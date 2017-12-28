from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from django.db.models import signals
from enumfields import Enum
from enumfields import EnumField
# from wiki.models.article import Article
from wiki.models import URLPath, Site, ArticleRevision, transaction, Article

from . import permissions


class BSI_Article_type(Enum):
    COMPONENT = 'C'
    THREAT = 'G'
    IMPLEMENTATIONNOTES = 'N'

    class Labels:
        COMPONENT = 'Components'
        THREAT = 'Threat'
        IMPLEMENTATIONNOTES = 'Implementation Notes'


class UGA(models.Model):
    url = models.OneToOneField(URLPath, on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create(cls, parent, slug, title, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        if not url.path.startswith('uga') or len(url.path) == 3:
            raise ValueError("A user article is supposed to be a child of 'uga' and it cannot be 'uga' itself.")
        uga = cls(url=url)
        uga.save()
        return url

    @classmethod
    def create_by_request(cls, request, article, parent, slug, title, content, summary):
        url = URLPath._create_urlpath_from_request(request=request, perm_article=article, parent_urlpath=parent,
                                                   slug=slug, title=title,
                                                   content=content, summary=summary)
        if not url.path.startswith('uga') or len(url.path) == 3:
            raise ValueError("A user article is supposed to be a child of 'uga' and it cannot be 'uga' itself.")
        uga = cls(url=url)
        uga.save()
        return url

    def add_link_to_bsi(self, bsi):
        bsi.references.add(self)

    def remove_link_from_bsi(self, bsi):
        bsi.references.remove(self)

    @classmethod
    def get_active_children(cls):
        parent = URLPath.get_by_path("uga/")
        return URLPath.objects.filter(parent=parent).exclude(Q(article__current_revision__deleted=True))

    def __str__(self):
        return 'UGA with path: ' + self.url.__str__()


class ArticleRevisionValidation(models.Model):
    revision = models.OneToOneField(ArticleRevision, on_delete=models.CASCADE, blank=False, null=False)
    validator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    status = models.BooleanField(default=False, blank=False, null=False)

    @classmethod
    def get_or_create(cls, instance, **kwargs):
        rev = None
        try:
            rev = ArticleRevisionValidation.objects.get(revision=instance)
        except ObjectDoesNotExist:
            rev = ArticleRevisionValidation.objects.create(revision=instance)
            rev.save()

        return rev

    @transaction.atomic
    def check_article(self, user):
        article = Article.objects.get(current_revision=self.revision)
        if permissions.can_check(article, user):
            self.status = True
            self.validator = user
            self.save()
        else:
            raise PermissionError("The user " + user.__str__() + " has no permissions to check this article.")

    @transaction.atomic
    def uncheck_article(self, user):
        article = Article.objects.get(current_revision=self.revision)
        if permissions.can_uncheck(article, user):
            self.status = False
            self.validator = user
            self.save()
        else:
            raise PermissionError("The user " + user.__str__() + " has no permissions to uncheck this article.")

    def __str__(self):
        return 'Revision validation for : ' + self.revision.__str__()


class BSI(models.Model):
    url = models.OneToOneField(URLPath, on_delete=models.CASCADE, primary_key=True)
    references = models.ManyToManyField(UGA, blank=True, related_name='is_linked_to')
    articleType = EnumField(BSI_Article_type, blank=True, max_length=1, null=True)

    @classmethod
    def get_or_create_bsi_root(cls, content):
        try:
            bsiRoot = URLPath.objects.get(slug='bsi')

        except URLPath.DoesNotExist:
            root = URLPath.objects.filter(slug=None)
            if (not root):
                site = Site.objects.get_current()
                kwargs = {'content': "", 'user_message': 'BSI.create', 'ip_address': '0.0.0.0'}
                root = URLPath.create_root(site=site, title="BSI Overview", request=None, **kwargs)
            else:
                root = root[0]
            rev_kwargs = {'content': content, 'user_message': 'BSI.create', 'ip_address': '0.0.0.0'}
            bsiRoot = URLPath.create_urlpath(parent=root, slug='bsi', title='BSI',
                                             **rev_kwargs)

        return bsiRoot

    @classmethod
    def get_or_create_bsi_subroots(cls, parent, slug, user_msg, content, title):
        subroot = URLPath.objects.filter(slug=slug, parent=parent)
        if (not subroot):
            rev_kwargs = {'content': content, 'user_message': user_msg, 'ip_address': '0.0.0.0'}
            subroot = URLPath.create_urlpath(parent=parent, slug=slug, title=title,
                                             **rev_kwargs)
        else:
            subroot = subroot[0]
        return subroot

    @classmethod
    @transaction.atomic
    def create(cls, parent, slug, title, article_type, **rev_kwargs):
        url = URLPath.create_urlpath(parent=parent, slug=slug, title=title, **rev_kwargs)
        # if not url.path.startswith('bsi') or len(url.path) == 3:
        #    raise ValueError("A bsi article is supposed to be a child of 'bsi' and it cannot be 'bsi' itself.")
        bsi = cls(url=url, articleType=article_type)
        bsi.save()

    @classmethod
    def get_articles_by_type(cls, article_type):
        article_urlpaths = []
        articles = BSI.objects.filter(articleType=article_type)
        if articles:
            bsi_root = BSI.get_or_create_bsi_root('')
            for article in articles:
                if article.url.parent.parent == bsi_root:
                    article_urlpaths.append(article.url)
        # return empty if nothing is found
        return article_urlpaths

    def __str__(self):
        return 'BSI article with path: ' + self.url.__str__()


signals.post_save.connect(ArticleRevisionValidation.get_or_create, sender=ArticleRevision)
