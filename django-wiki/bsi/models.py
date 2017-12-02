from django.db import models
from wiki.models.article import Article
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class ArticleAttr(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    isArchive = models.BooleanField(default=False)
    reference_id = models.ForeignKey(Article, blank=True, related_name='is_linked_to')
    bsi_id = models.CharField(max_length=10, blank=True)

    def isThreat(self):
        return self.bsi_id.startswith('G')

    def isComponent(self):
        return self.bsi_id.startswith('B')

    def isCountermeasure(self):
        return self.bsi_id.startswith('M')

    def isBSIArticle(self):
        return bool(self.bsi_id);

    def isUserArticle(self):
        return not self.bsi_id;


@receiver(post_save, sender=Article)
def create_article_attr(sender, instance, created, **kwargs):
    if created:
        ArticleAttr.objects.create(article=instance)


@receiver(post_save, sender=Article)
def save_article_attr(sender, instance, **kwargs):
    instance.articleattr.save()
