from django.db import models
#from wiki.models.article import Article
from wiki.models import Article, URLPath, Site, ArticleRevision
from enumfields import EnumField
from enumfields import Enum

class BSI_Article_type(Enum):
    COMPONENT = 'C'
    THREAT = 'G'
    COUNTERMEASURE = 'M'

# Create your models here.
class UGA(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)


class BSI(models.Model):
   # article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)
    #bsi_id = models.CharField(max_length=10, blank=True)
    url = models.OneToOneField('wiki.URLPath')
    references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')
    articleType = EnumField(BSI_Article_type,blank=True, max_length=1)

    def isThreat(self):
        return self.url.slug.startswith('G')

    def isComponent(self):
        return self.url.slug.startswith('B')

    def isCountermeasure(self):
        return self.url.slug.startswith('M')


