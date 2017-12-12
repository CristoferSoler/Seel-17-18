from django.conf.urls import url
from wiki.models import URLPath

from . import views, ugaViews

from wiki.views import article
from .views import BSISearchView, BSIArticleView, UGACreate, CreateRoot

article_create_view_class = article.Create

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^create-root/$', CreateRoot.as_view(), name='root_create'),
    url(r'^search/', BSISearchView.as_view(), name='bsisearch'),
    url(r'^article/(?P<path>.+/|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^article/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^(?P<article_id>[0-9]+|)/$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^bsi/threats/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^bsi/components/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    url(r'^(?P<path>.+/|)_createArticle/$', UGACreate.as_view(), name='create'),
    url(r'ugarticles/', ugaViews.overviewUGA, name='ugarticles'),

    url(r'^(?P<path>.+/|)_create/', views.UGACreate.as_view(), name='create'),
    url(r'^(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
]
