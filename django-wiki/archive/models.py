from django.db import models
from wiki.models import Article, URLPath


# Create your models here.

class ArchivedArticle(models.Model):
    article = models.OneToOneField('Article', verbose_name=_('archived article'),
                                   blank=True, null=True, related_name='archived',
                                   help_text=_(
                                       'Article that has been archived.'), on_delete=models.CASCADE, )

    archive = models.OneToOneField('Archive', verbose_name=_('related archive'),
                                   blank=False, null=False, related_name='belongig_to',
                                   help_text=_(
                                       'Archive which contains this archived article.'), on_delete=models.CASCADE, )


class Archive(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created'),
    )

    url = URLPath.create_urlpath()