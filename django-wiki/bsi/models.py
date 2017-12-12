from django.db import models
# from wiki.models.article import Article
from wiki.models import Article, URLPath, Site, ArticleRevision


class UGA(models.Model):
    urlpath = models.OneToOneField(URLPath, on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create(cls, parent, slug, title, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        if not url.path.startswith('uga') or len(url.path) == 3:
            raise ValueError("A user article is supposed to be a child of 'uga' and it cannot be 'uga' itself.")
        uga = cls(urlpath=url)
        uga.save()

    def add_link_to_bsi(self, bsi):
        bsi.references.add(self)

    def remove_link_from_bsi(self, bsi):
        bsi.references.remove(self)

    def __str__(self):
        return 'UGA with path: ' + self.urlpath.__str__()


class BSI(models.Model):
    urlpath = models.OneToOneField('wiki.URLPath', on_delete=models.CASCADE, )
    references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')

    @classmethod
    def create(cls, parent, slug, title, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        if not url.path.startswith('bsi') or len(url.path) == 3:
            raise ValueError("A bsi article is supposed to be a child of 'bsi' and it cannot be 'bsi' itself.")
        bsi = cls(urlpath=url)
        bsi.save()

    def __str__(self):
        return 'BSI article with path: ' + self.urlpath.__str__()

    # def isThreat(self):
    #     return self.url.slug.startswith('G')
    #
    # def isComponent(self):
    #     return self.url.slug.startswith('B')
    #
    # def isCountermeasure(self):
    #     return self.url.slug.startswith('M')
