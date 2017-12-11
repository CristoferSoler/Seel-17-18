from django.conf.urls import url
from wiki.models import URLPath
from .views import ArchiveDir, ArchiveArticleView

urlpatterns = [
    # if path='' it is root
    url(r'^(?P<path>[^/]+(/|)|)$', ArchiveDir.as_view(), name='archive_dir'),
    # to display archive article
    url(r'^(?P<path>.+)/(?P<article_id>\d+)(/|)$', ArchiveArticleView.as_view(), name='archive_art_get'),
]
