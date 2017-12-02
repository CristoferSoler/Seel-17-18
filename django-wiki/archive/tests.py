from django.test import TestCase
from wiki.models import Article, ArticleRevision, URLPath, Site
from archive.models import Archive


# Create your tests here.
class ArchiveTestCase(TestCase):
    def setUp(self):
        ArchiveTestCase.createRoot(rev_title="root")
        ArchiveTestCase.createArticle(rev_title="subarticle1", slug="subarticle1")
        # todo create archive here <- implement create function in models or views

    def test_article_moved_to_archive(self):
        articleId = URLPath.objects.filter(slug='subarticle1').values_list('article')[0]
        article = Article.objects.get(pk=articleId[0])
        parentId = URLPath.objects.filter(slug='subarticle1').values_list('parent')[0]
        parent = Article.objects.get(pk=parentId[0])
        rootId = URLPath.objects.filter(slug=None).values_list('article')[0]
        root = Article.objects.get(pk=rootId[0])
        self.assertTrue(parent == root, "article 'parent' should be the root")

    @classmethod
    def createRoot(cls, rev_title):
        revision_kwargs = {'content': 'content', 'user_message': 'Crawler input', 'ip_address': 'None'}
        site = Site.objects.get_current()

        article_kwargs = {}
        article = Article(**article_kwargs)
        article.add_revision(ArticleRevision(title=rev_title, **revision_kwargs),
                             save=True)
        article.save()
        newpath = URLPath.objects.create(
            site=site,
            parent=None,
            slug=None,
            article=article)

        article.add_object_relation(newpath)

    @classmethod
    def createArticle(cls, rev_title, slug):
        revision_kwargs = {'content': 'content', 'user_message': 'Crawler input', 'ip_address': 'None'}
        parent = URLPath.objects.filter(slug=None)[0]

        site = Site.objects.get_current()

        article_kwargs = {}
        article = Article(**article_kwargs)
        article.add_revision(ArticleRevision(title=rev_title, **revision_kwargs),
                             save=True)
        article.save()
        newpath = URLPath.objects.create(
            site=site,
            parent=parent,
            slug=slug,
            article=article)

        article.add_object_relation(newpath)
