import os
from operator import itemgetter
from django.contrib.auth import login, authenticate
import pdb
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.core.mail import EmailMessage
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from archive.models import Archive
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
#from wiki.decorators import get_article
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from .decorators import get_article
from wiki.models import URLPath, models
from wiki.models.article import Article
from wiki.views.article import ArticleView
from wiki.views.article import SearchView
from .models.article_extensions import BSI_Article_type
from .forms import FilterForm, UserRegistrationForm
from wiki import models
from django.contrib import admin
from bsi.models import BSI_Article_type
from bsi.ugaViews import overview_uga
from django.contrib.admin.sites import AdminSite
from .models.article_extensions import BSI
from .wizard import readAndProcessCSV,getListOfFrequenceOfTopic
import csv
import json
import itertools
from collections import Counter
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token

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
        elif path.startswith('new'):
            self.template_name = "bsi/update-list.html"

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
        self.filter_form = FilterForm(request.GET)
        if self.filter_form.is_valid():
            self.filter = self.filter_form.cleaned_data['f']
            assert (int(self.filter) > 0 and int(self.filter) < 6)
        else:
            self.filter = None
        return super(BSISearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        #import pdb
        #pdb.set_trace()
        search_result = super(BSISearchView, self).get_queryset()
        # store the ids only
        filtered_result = []
        if (not self.filter) or (self.filter == '1'):
            return search_result
        for article in search_result:
            url = URLPath.objects.get(article=article)
            if url.parent.parent == Archive.get_or_create_archive_root():
                if self.filter == '5':
                    filtered_result.append(article.pk)
                continue
            if hasattr(url, 'bsi'):
                if self.filter == '2':
                    if url.bsi.articleType == BSI_Article_type.COMPONENT:
                        filtered_result.append(article.pk)
                elif self.filter == '3':
                    if url.bsi.articleType == BSI_Article_type.THREAT:
                        filtered_result.append(article.pk)
                elif self.filter == '4':
                    if url.bsi.articleType == BSI_Article_type.IMPLEMENTATIONNOTES:
                        filtered_result.append(article.pk)
        return search_result.filter(id__in=filtered_result)

    def get_context_data(self, **kwargs):
        k = super(BSISearchView, self).get_context_data(**kwargs)
        k['filter'] = self.filter
        return k

def index(request):
    components = readAndProcessCSV()
    sortedTopics = getListOfFrequenceOfTopic(components['components'])
    template = loader.get_template('bsi/index.html')
    componentsString = json.dumps(components)
    sortedTopicsString = json.dumps(sortedTopics)
    new_page = check_new_page()

    return HttpResponse(template.render({'newpage':new_page,'components':componentsString,'sortedTopics':sortedTopicsString},request))


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
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Seel Account'
            message = render_to_string('bsi/account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'bsi/account/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return redirect('index')
    else:
        #TODO
        return HttpResponse('Activation link is invalid!')


def create(request):
    return render(request, 'bsi/create_article.html')

def about(request):
    return render(request, 'bsi/footer/about.html')

def faq(request):
    return render(request, 'bsi/footer/faq.html')

def contact(request):
    return render(request, 'bsi/footer/contact.html')

def check_new_page():
    try:
        URLPath.objects.get(slug='new')
        return True
    except:
        return False

