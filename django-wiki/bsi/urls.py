from django.conf.urls import url
from wiki.views import article

from . import views
from .ugaViews import CreateRoot, UGEditView, UGACreate
from .views import BSISearchView, WikiArticleView

article_create_view_class = article.Create

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^create-root/$', CreateRoot.as_view(), name='root_create'),
    url(r'^search/$', BSISearchView.as_view(), name='bsisearch'),
    url(r'^search/$', BSISearchView.as_view(), name='bsifilter'),
    # url(r'^article/(?P<path>.+/|)$', WikiArticleView.as_view(), name='bsiarticle'),
    # url(r'^article/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^(?P<article_id>[0-9]+|)/$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^bsi/threats/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^bsi/components/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^(?P<path>.+/|)_createArticle/$', UGACreate.as_view(), name='create'),
    # url(r'^uga/$', overview_uga, name='uga'),
    # url(r'^(?P<path>.+/|)$', WikiArticleView.as_view(), name='display_uga'),

    url(r'^(?P<path>.+/|)edit/$', UGEditView.as_view(), name='edit'),
    # the following url handles any article! The template that should be used is depending from the url, see WikiArticleView
    url(r'^(?P<path>.+/|)_create/', UGACreate.as_view(), name='create'),
    url(r'^(?P<path>.+|)$', WikiArticleView.as_view(), name='get_article'),
    # url(r'^(?P<path>.+/|)_edit/$', UGEditView.as_view(), name='edit'),

]
