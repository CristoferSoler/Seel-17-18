from django.conf.urls import url
from django.views.generic import TemplateView
from wiki.views import article

from . import ugaViews
from . import views
from .ugaViews import CreateRoot, UGEditView, UGACreate, UGDeleteView, UGHistoryView, UGPreviewView, \
    UGChangeRevisionView
from .views import BSISearchView, WikiArticleView

article_create_view_class = article.Create
# article_diff_view = staticmethod(ugaViews.diff)

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots_file"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^$', views.index, name='index'),
    # url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^create-root/?$', CreateRoot.as_view(), name='root_create'),
    url(r'^search/?$', BSISearchView.as_view(), name='bsisearch'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^faq/?$', views.faq, name='faq'),
    url(r'^contact/?$', views.contact, name='contact'),
    # url(r'^new/?$', WikiArticleView.as_view(), name='new'),
    # url(r'^article/(?P<path>.+/|)$', WikiArticleView.as_view(), name='bsiarticle'),
    # url(r'^article/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^(?P<article_id>[0-9]+|)/$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^bsi/threats/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^bsi/components/(?P<path>.+|)$', BSIArticleView.as_view(), name='bsiarticle'),
    # url(r'^(?P<path>.+/|)_createArticle/$', UGACreate.as_view(), name='create'),
    # url(r'^uga/$', overview_uga, name='uga'),
    # url(r'^(?P<path>.+/|)$', WikiArticleView.as_view(), name='display_uga'),

    url(r'^(?P<path>.+/|)edit/$', UGEditView.as_view(), name='edit'),
    url(r'^(?P<path>.+/|)history/$', UGHistoryView.as_view(), name='history'),
    # url(r'^(?P<article_id>\d+)/history/$', UGHistoryView.as_view(), name='history'),
    # url(r'^(?P<path>.+/|)_history/$', UGHistoryView.as_view(), name='history'),
    url(r'^_revision/diff/(?P<revision_id>[0-9]+)/$', ugaViews.diff, name='diff'),
    url(r'^_revision/preview/(?P<article_id>\d+)/$', UGPreviewView.as_view(), name='preview_revision'),
    url(r'^(?P<path>.+/|)_revision/change/(?P<revision_id>\d+)/$', UGChangeRevisionView.as_view(),
        name='change_revision'),
    url(r'^(?P<path>.+/|)delete/$', UGDeleteView.as_view(), name='delete'),
    # the following url handles any article! The template that should be used is depending from the url, see WikiArticleView
    url(r'^(?P<path>.+/|)_create/$', UGACreate.as_view(ugaViews.FORMS), name='create'),
    url(r'^uga/_create/get_bsi_articles/$', ugaViews.get_bsi_articles, name='get_bsi_articles'),
    # url(r'^(?P<path>.+/|)_create/_add_links/$', UGCreateAddLinksView.as_view(), name='add_links'),
    url(r'^(?P<path>.+|)$', WikiArticleView.as_view(), name='get_article'),

]
