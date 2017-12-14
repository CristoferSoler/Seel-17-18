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
    url = models.OneToOneField(URLPath, on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create(cls, parent, slug, title, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        if not url.path.startswith('uga') or len(url.path) == 3:
            raise ValueError("A user article is supposed to be a child of 'uga' and it cannot be 'uga' itself.")
        uga = cls(urlpath=url)
        uga.save()

   # def add_link_to_bsi(self, bsi):
   #     bsi.references.add(self)

   # def remove_link_from_bsi(self, bsi):
   #     bsi.references.remove(self)

    def __str__(self):
        return 'UGA with path: ' + self.urlpath.__str__()

class BSI(models.Model):
   # article = models.OneToOneField(Article, on_delete=models.CASCADE, primary_key=True)
    #bsi_id = models.CharField(max_length=10, blank=True)
    url = models.OneToOneField(URLPath, on_delete=models.CASCADE, primary_key=True)
    #references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')
    articleType = EnumField(BSI_Article_type,blank=True, max_length=1)

    @classmethod
    def get_or_create_bsi_root(cls, content):
        try:
            root = URLPath.objects.get(slug='bsi')
        except URLPath.DoesNotExist:
            rev_kwargs = {'content': content, 'user_message': 'BSI.create', 'ip_address': '0.0.0.0'}
            root = URLPath.create_urlpath(parent=URLPath.objects.get(slug=None), slug='bsi', title='BSI',
                                   **rev_kwargs)
        return root

    @classmethod
    def get_or_create_bsi_subroots(cls, slug, user_msg, content, title):
        bsi_root = BSI.get_or_create_bsi_root('')
        subroot = URLPath.objects.filter(slug=slug)
        if (not subroot):
            rev_kwargs = {'content': content, 'user_message': user_msg, 'ip_address': '0.0.0.0'}
            root = URLPath.create_urlpath(parent=bsi, slug=slug, title=title,
                                        **rev_kwargs)
        return subroot

    @classmethod
    @transaction_atomic
    def create(cls, parent, slug, title, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        if not url.path.startswith('bsi') or len(url.path) == 3:
            raise ValueError("A bsi article is supposed to be a child of 'bsi' and it cannot be 'bsi' itself.")
        bsi = cls(urlpath=url)
        bsi.save()

    def __str__(self):
        return 'BSI article with path: ' + self.urlpath.__str__() 

