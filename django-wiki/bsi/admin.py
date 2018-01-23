from django.contrib.sites.models import Site
from django.contrib import admin
from wiki.models import ArticleRevision, Article, URLPath
from wiki.plugins.images.models import Image
from wiki.plugins.attachments.models import Attachment


admin.site.unregister(Site)
admin.site.unregister(ArticleRevision)
admin.site.unregister(Article)
admin.site.unregister(URLPath)
admin.site.unregister(Image)
admin.site.unregister(Attachment)