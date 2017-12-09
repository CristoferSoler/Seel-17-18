from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
#from .models import <tableName>
# from bsi.core.paginator import WikiPaginator
from wiki.models.article import Article
#from wiki.tests.test_views import SearchViewTest
from wiki.views.article import SearchView
from wiki.views.article import ArticleView, CreateRootView
from wiki.views.article import SearchView, Create
from wiki import forms

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from wiki.decorators import get_article
from django.utils.decorators import method_decorator

from django import forms
from wiki.views.mixins import ArticleMixin


class CreateRoot(CreateRootView):
    template_name="uga/create-root.html"
    def dispatch(self, request, *args, **kwargs):
        return super(CreateRoot, self).dispatch(request, *args, **kwargs)



class UGACreate(Create):
    template_name = 'uga/create_article.html'

    @method_decorator(get_article(can_write=True, can_create=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super(Create, self).dispatch(request, article, *args, **kwargs)

class BSIArticleView(ArticleView):
    template_name = "bsi/article.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super(
            ArticleView,
            self).dispatch(
            request,
            article,
            *args,
            **kwargs)

# Create your views here.
