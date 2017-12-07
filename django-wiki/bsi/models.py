from django.db import models
from wiki.models.article import Article


# Create your models here.
class UGA(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)


class BSI(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)
    bsi_id = models.CharField(max_length=10, blank=True)
    references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')

    def isThreat(self):
        return self.bsi_id.startswith('G')

    def isComponent(self):
        return self.bsi_id.startswith('B')

    def isCountermeasure(self):
        return self.bsi_id.startswith('M')



