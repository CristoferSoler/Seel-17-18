import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import redirect, get_object_or_404
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.utils.http import urlquote

from functools import wraps

from six.moves import filter

from wiki.core.exceptions import NoRootURL
from wiki.conf import settings
import pdb

def get_archive_article(func=None, can_read=True, deleted_contents=False):

    def wrapper(request, *args, **kwargs):
        from . import models
        #pdb.set_trace()
        path = kwargs.pop('path', None)
        article_id = kwargs.pop('article_id', None)
        
        # append archive to the beginning of path
        path = "archive/" + path.lstrip("/")
        urlpath = None
        
        # fetch by urlpath.path
        if not path is None:
            try:
                urlpath = models.URLPath.get_by_path(path, select_related=True)
            except NoRootURL:
                return redirect('wiki:root_create')
            except models.URLPath.DoesNotExist:
                raise Http404("No archive found that matches the specified path: ", path)
                '''
                try:
                    pathlist = list(filter(lambda x: x!="", path.split("/"),))
                    path = "/".join(pathlist[:-1])
                    parent = models.URLPath.get_by_path(path)
                    return HttpResponseRedirect(reverse("wiki:create", kwargs={'path': parent.path,}) + "?slug=%s" % pathlist[-1])
                except models.URLPath.DoesNotExist:
                    c = RequestContext(request, {'error_type' : 'ancestors_missing'})
                    return HttpResponseNotFound(render_to_string("wiki/error.html", context_instance=c))
                '''
            if urlpath.article:
                # urlpath is already smart about prefetching items on article (like current_revision), so we don't have to
                article = urlpath.article
            else:
                # Be robust: Somehow article is gone but urlpath exists... clean up
                return_url = reverse('wiki:get', kwargs={'path': urlpath.parent.path})
                urlpath.delete()
                return HttpResponseRedirect(return_url)
        
        '''
        # fetch by article.id
        elif article_id:
            #TODO We should try to grab the article form URLPath so the caching is good, and fall back to grabbing it from Article.objects if not
            articles = models.Article.objects
            
            article = get_object_or_404(articles, id=article_id)
            try:
                urlpath = models.URLPath.objects.get(articles__article=article)
            except models.URLPath.DoesNotExist as noarticle:
                models.URLPath.MultipleObjectsReturned = noarticle
                urlpath = None
        
        
        else:
            raise TypeError('You should specify either article_id or path')
        '''

        if not deleted_contents:    
            # If the article has been deleted, show a special page.        
            if urlpath:
                if urlpath.is_deleted(): # This also checks all ancestors
                    return redirect('wiki:deleted', path=urlpath.path)
            '''
            else:
                if article.current_revision and article.current_revision.deleted:
                    return redirect('wiki:deleted', article_id=article.id)
            
        
        if article.current_revision.locked and not_locked:
            return response_forbidden(request, article, urlpath)

        if can_read and not article.can_read(request.user):
            return response_forbidden(request, article, urlpath)
        
        if (can_write or can_create) and not article.can_write(request.user):
            return response_forbidden(request, article, urlpath)

        if can_create and not (request.user.is_authenticated() or settings.ANONYMOUS_CREATE):
            return response_forbidden(request, article, urlpath)
        
        if can_delete and not article.can_delete(request.user):
            return response_forbidden(request, article, urlpath)
            
        if can_moderate and not article.can_moderate(request.user):
            return response_forbidden(request, article, urlpath)
        '''

        kwargs['urlpath'] = urlpath
        
        return func(request, article, *args, **kwargs)
    
    if func:
        return wrapper
    else:
        return lambda func: get_archive_article(func, can_read=can_read, deleted_contents=deleted_contents)
