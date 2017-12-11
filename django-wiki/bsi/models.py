from django.db import models
#from wiki.models.article import Article
from wiki.models import Article, URLPath, Site, ArticleRevision


# Create your models here.
class UGA(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)


class BSI(models.Model):
   # article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)
    #bsi_id = models.CharField(max_length=10, blank=True)
    url = models.OneToOneField('wiki.URLPath')
    references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')

    def isThreat(self):
        return self.url.slug.startswith('G')

    def isComponent(self):
        return self.url.slug.startswith('B')

    def isCountermeasure(self):
        return self.url.slug.startswith('M')