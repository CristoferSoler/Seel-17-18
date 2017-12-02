from django.db import models
from wiki.models import Article, URLPath


# Create your models here.

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

class Archive(Article):
    def archiveArticle(self, article):
        """

        """

        article.urlpath.parent = self.urlpath
        # article.urlpath.slug = form.cleaned_data['slug']
        article.urlpath.save()

        # Reload url path from database
        article.urlpath = models.URLPath.objects.get(pk=article.urlpath.pk)

        # Use a copy of ourself (to avoid cache) and update article links again
        for ancestor in models.Article.objects.get(pk=article.pk).ancestor_objects():
            ancestor.article.clear_cache()
