
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import <tableName>
# from bsi.core.paginator import WikiPaginator
from wiki.models.article import Article
from wiki.views.article import SearchView


def index(request):
    all_articles = Article.objects.all()

    template = loader.get_template('bsi/index.html')
    context = {
        'all_articles':all_articles,
    }
    return HttpResponse(template.render(context, request))

