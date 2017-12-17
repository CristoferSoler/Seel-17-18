import os
from operator import itemgetter

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.utils.decorators import method_decorator
from wiki.decorators import get_article
from wiki.models.article import Article
from wiki.views.article import ArticleView
from wiki.views.article import SearchView
import csv
import json
import itertools
from collections import Counter

from bsi.ugaViews import overview_uga


class WikiArticleView(ArticleView):

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        """
        The dispatch method decides which template is used to display an article. Depending from its parent (uga or bsi) different templates will be used.
        """
        urlpath = kwargs.get('urlpath')
        if not urlpath:
            raise Http404("No urlpath specified")
        path = urlpath.path
        slug = urlpath.slug

        if path.startswith('uga') and len(path) == 4:
            self.template_name = "uga/overview_uga.html"
            return overview_uga(request)
        elif path.startswith('uga'):
            self.template_name = "uga/view.html"
        elif path.startswith('bsi'):
            self.template_name = "bsi/article.html"
        elif path.startswith('news'):
            """ todo set news template """

        return super(
            ArticleView,
            self).dispatch(
            request,
            article,
            *args,
            **kwargs)


class BSISearchView(SearchView):
    template_name = "bsi/search.html"

    def dispatch(self, request, *args, **kwargs):
        return super(BSISearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(BSISearchView, self).get_queryset()

    def get_context_data(self, **kwargs):
        return super(BSISearchView, self).get_context_data(**kwargs)

def getListOfFrequenceOfTopic(components):
    topics = []
    listOfAllTopics = []
    for component in components:
        listOfAllTopics = itertools.chain(listOfAllTopics, component['topics'])
    listOfAllTopics = list(listOfAllTopics)
    numberOfEachTopic = list(Counter(listOfAllTopics).items())
    numberOfEachTopic = sorted(numberOfEachTopic, key=itemgetter(1), reverse=True)
    for topic in numberOfEachTopic:
        topics.append(topic[0])
    return topics

def index(request):
    components = readAndProcessCSV()
    sortedTopics = getListOfFrequenceOfTopic(components['components'])
    template = loader.get_template('bsi/index.html')
    componentsString = json.dumps(components)
    sortedTopicsString = json.dumps(sortedTopics)

    return HttpResponse(template.render({'components':componentsString,'sortedTopics':sortedTopicsString},request))

def generateDic(list):
    componentDic = {'name':list[0],'topics':list[1:]}
    return componentDic

def readAndProcessCSV():
    componentsWithTopics = {'components':[]}
    with open('./bsi/static/bsi/csv/topics.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            componentsWithTopics['components'].append(generateDic(row))
    return componentsWithTopics

def bsicatalog(request):
    all_articles = Article.objects.all()

    template = loader.get_template('bsi/article.html')
    context = {
        'all_articles': all_articles,
    }
    return HttpResponse(template.render(context, request))


@login_required
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'bsi/account/register.html', {'form': form})


def create(request):
    return render(request, 'bsi/create_article.html')
