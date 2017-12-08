"""bsiwiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
from archive import views
from wiki.views.article import Dir, ArticleView

# class BSIWikiUrlPattern(object):
#archive_root_view_class = views.ArchiveRoot
archive_dir_view_class = views.ArchiveDir

# def get_urls(self):
#     urlpatterns = self.get_root_urls()
# urlpatterns += self.get_article_path_urls()
# return urlpatterns


# @staticmethod
# def get_root_urls():
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notifications/', get_nyt_pattern()),
    # todo if the url archive/ is called, the wiki should list (_dir) all sub-archives
    # url(r'^archive/$', archive_dir_view_class.as_view(),
    #     name='archive_root'),
    
    url(r'^archive/', include('archive.urls')),
    url(r'', get_wiki_pattern()),
]
# return urlpatterns


# def get_article_path_urls(self):
#     urlpatterns = [
#     ]
#     return urlpatterns
