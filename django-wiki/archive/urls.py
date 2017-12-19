
from django.conf.urls import url
from .views import ArchiveArticleView, overview_archive

urlpatterns = [
    url(r'^(?P<path>[^/]+)/(?P<article>.+)/$', ArchiveArticleView.as_view(), name='archive_get'),
    #url(r'^(?P<path>[^/]+(/|)|)$', ArchiveDir.as_view(), name='archive_dir'),
    url(r'^(?P<path>[^/]+(/|)|)$', overview_archive, name='archive_dir'),
]
