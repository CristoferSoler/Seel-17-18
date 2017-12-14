from django.db import models , IntegrityError
#from wiki.models.article import Article
from wiki.models import Article, URLPath, Site, ArticleRevision, transaction
from enumfields import EnumField
from enumfields import Enum
from django.http import Http404


class BSI_Article_type(Enum):
    COMPONENT = 'C'
    THREAT = 'G'
    IMPLEMENTATIONNOTES = 'N'

# Create your models here.
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
    url = models.OneToOneField(URLPath, on_delete=models.CASCADE, primary_key=True)
    references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')
    articleType = EnumField(BSI_Article_type,blank=True, max_length=1, null = True)

    @classmethod
    def get_or_create_bsi_root(cls, content):
        try:
           bsiRoot = URLPath.objects.get(slug='bsi')

        except URLPath.DoesNotExist:
            root = URLPath.objects.filter(slug=None)
            if (not root):
                site = Site.objects.get_current()
                kwargs = {'content': "", 'user_message': 'BSI.create', 'ip_address': '0.0.0.0'}
                root = URLPath.create_root(site=site, title="Root", request=None, **kwargs)
            else:
                root = root[0]
            rev_kwargs = {'content': content, 'user_message': 'BSI.create', 'ip_address': '0.0.0.0'}
            bsiRoot = URLPath.create_urlpath(parent=root, slug='bsi', title='BSI',
                                                **rev_kwargs)

        return bsiRoot

    @classmethod
    def get_or_create_bsi_subroots(cls, slug, user_msg, content, title):
        bsi_root = BSI.get_or_create_bsi_root('')
        subroot = URLPath.objects.filter(slug=slug)
        if (not subroot):
            rev_kwargs = {'content': content, 'user_message': user_msg, 'ip_address': '0.0.0.0'}
            subroot = URLPath.create_urlpath(parent=bsi_root, slug=slug, title=title,
                                        **rev_kwargs)
        else:
            subroot = subroot[0]
        return subroot

    @classmethod
    @transaction.atomic
    def create(cls, parent, slug, title, article_type, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        if not url.path.startswith('bsi') or len(url.path) == 3:
            raise ValueError("A bsi article is supposed to be a child of 'bsi' and it cannot be 'bsi' itself.")
        bsi = cls(url=url, articleType=article_type)
        bsi.save()

    @classmethod
    def get_articles_by_type(cls, article_type):
         article_urlpaths = []
         articles = BSI.objects.filter(articleType= article_type)
         if not articles:
             raise Http404("No articles found that matches the specified search type: ", article_type)
         for article in articles:
             article_urlpaths.append(article)
         return article_urlpaths


    def __str__(self):
        return 'BSI article with path: ' + self.url.__str__()

