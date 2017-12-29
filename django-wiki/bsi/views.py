import pdb

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

from bsi.models import BSI_Article_type
from bsi.ugaViews import overview_uga
from .models.article_extensions import BSI


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
            self.template_name = "uga/overview_base.html"
            return overview_uga(request)
        elif path.startswith('uga'):
            self.template_name = "uga/view.html"
        elif path.startswith('bsi'):
            self.template_name = "bsi/article_bsi.html"
        elif path.startswith('news'):
            """ todo set news template """

        return super(
            ArticleView,
            self).dispatch(
            request,
            article,
            *args,
            **kwargs)

    def post(self, request, *args, **kwargs):
        pass


class BSISearchView(SearchView):
    template_name = "bsi/searchresult.html"

    def dispatch(self, request, *args, **kwargs):
        return super(BSISearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(BSISearchView, self).get_queryset()

    def get_context_data(self, **kwargs):
        return super(BSISearchView, self).get_context_data(**kwargs)


class BSIFilterView(SearchView):
    template_name = "bsi/searchresult.html"

    def get_queryset(self):
        pdb.set_trace()
        filter_category = self.request.GET.get("filter_category")
        article_urlpaths = []
        if (filter_category == 'G'):
            cat = BSI_Article_type.THREAT
        articles = BSI.objects.filter(articleType=cat)
        if not articles: return
        if articles:
            for article in articles:
                article_urlpaths.append(article.url.article)
        # return empty if nothing is found
        return article_urlpaths


def index(request):
    all_articles = Article.objects.all()

    template = loader.get_template('bsi/index.html')
    context = {
        'all_articles': all_articles,
    }
    return HttpResponse(template.render(context, request))


def bsicatalog(request):
    all_articles = Article.objects.all()

    template = loader.get_template('bsi/article_base.html')
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
