from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.db.models import Q
from wiki import forms
from wiki.core.paginator import WikiPaginator
from wiki.decorators import get_article
from wiki.models.urlpath import URLPath
from wiki.views.article import Dir
from wiki.views.mixins import ArticleMixin
from .models import Archive


class ArchiveDir(Dir):
    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        # find archive by urlpath slug, if it is not present, 404 will occur
        Archive.get_archive_by_slug(kwargs.get('urlpath').slug)

        return super(Dir, self).dispatch(request, article, *args, **kwargs)
