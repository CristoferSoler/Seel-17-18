from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.db.models import Q
from wiki import forms
#from wiki.core.paginator import WikiPaginator
from wiki.decorators import get_article
from wiki.models.urlpath import URLPath
from wiki.views.article import Dir, ArticleView
from wiki.views.mixins import ArticleMixin
from .models import Archive
from .decorators import get_archive_article
import pdb

class ArchiveDir(Dir):
    template_name = "archive/dir.html"    

    @method_decorator(get_archive_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        # find archive by urlpath slug, if it is not present, 404 will occur
        path = kwargs.get('urlpath')
        if(path != Archive.get_archive_root()):
            Archive.get_archive_by_slug(kwargs.get('urlpath').slug)
       
        # temp fix 
        self.filter_form = forms.DirFilterForm(request.GET)
        if self.filter_form.is_valid():
            self.query = self.filter_form.cleaned_data['query']
        else:
            self.query = None

        return super(Dir, self).dispatch(request, article, *args, **kwargs)

    def get_queryset(self):
        return super(ArchiveDir, self).get_queryset()

    def get_context_data(self, **kwargs):
        return super(ArchiveDir, self).get_context_data(**kwargs)

class ArchiveArticleView(ArticleView):
    
    def dispatch(self, request, article, *args, **kwargs):
        # check ArchiveTransactionHere
        #pdb.set_trace()        

        return super(ArticleView, self).dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(ArchiveArticleView, self).get_context_data(**kwargs)




