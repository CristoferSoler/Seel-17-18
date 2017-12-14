from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from .models import Archive

def get_archive_article(func=None, can_read=True, deleted_contents=False):

    def wrapper(request, *args, **kwargs):
        from . import models
        path = kwargs.pop('path', None)
        article_id = kwargs.pop('article_id', None)
        
        path = path.rstrip("/")
        urlpath = None
        
        # fetch by urlpath.path
        if not path is None:
            try:
                if(path == ''):
                    urlpath = Archive.get_or_create_archive_root()
                else:
                    urlpath = Archive.get_archive_by_slug(path).archive_url
            except models.URLPath.DoesNotExist:
                raise Http404("No archive found that matches the specified path: ", path)
            if urlpath.article:
                # urlpath is already smart about prefetching items on article (like current_revision), so we don't have to
                article = urlpath.article
            else:
                # Be robust: Somehow article is gone but urlpath exists... clean up
                return_url = reverse('wiki:get', kwargs={'path': urlpath.parent.path})
                urlpath.delete()
                return HttpResponseRedirect(return_url)
        
        if not deleted_contents:    
            # If the article has been deleted, show a special page.        
            if urlpath:
                if urlpath.is_deleted(): # This also checks all ancestors
                    return redirect('wiki:deleted', path=urlpath.path)

        kwargs['urlpath'] = urlpath
        
        return func(request, article, *args, **kwargs)
    
    if func:
        return wrapper
    else:
        return lambda func: get_archive_article(func, can_read=can_read, deleted_contents=deleted_contents)
