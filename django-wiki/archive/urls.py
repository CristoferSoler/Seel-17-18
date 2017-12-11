from django.conf.urls import url
from .views import ArchiveDir, ArchiveArticleView

urlpatterns = [
    url(r'^(?P<path>[^/]+)/(?P<article>.+)/$', ArchiveArticleView.as_view(), name='archive_get'),
    url(r'^(?P<path>[^/]+(/|)|)$', ArchiveDir.as_view(), name='archive_dir'),
]




