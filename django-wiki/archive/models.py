from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from wiki.decorators import get_article
from wiki.models.urlpath import URLPath, transaction
from wiki.models.article import Article
from wiki.views.mixins import ArticleMixin


# class ArchivedArticle(models.Model):
#     article = models.OneToOneField('Article', verbose_name=_('archived article'),
#                                    blank=True, null=True, related_name='archived',
#                                    help_text=_(
#                                        'Article that has been archived.'), on_delete=models.CASCADE, )
#
#     archive = models.OneToOneField('Archive', verbose_name=_('related archive'),
#                                    blank=False, null=False, related_name='belongig_to',
#                                    help_text=_(
#                                        'Archive which contains this archived article.'), on_delete=models.CASCADE, )
#


class ArchiveTransaction(models.Model):
    archive_root = models.OneToOneField('wiki.URLPath', verbose_name='archive parent article',
                                        blank=False, null=False, related_name='archive_root_article',
                                        on_delete=models.CASCADE, )

    @classmethod
    def create(cls, urlpath):
        return cls(archive_root=urlpath)

    # @transaction.atomic
    def archive(self, urlpath):

        # urlpath.slug = new_slug
        urlpath.parent = self.archive_root
        urlpath.save()

        # self.urlpath.parent = parent
        # self.urlpath.slug = slug
        # self.urlpath.save()

        # Reload url path form database
        urlpath = URLPath.objects.get(pk=urlpath.pk)

        # Use a copy of ourself (to avoid cache) and update article links again
        for ancestor in Article.objects.get(pk=urlpath.article.pk).ancestor_objects():
            ancestor.article.clear_cache()
