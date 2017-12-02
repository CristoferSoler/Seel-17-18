from django.db.models.base import ModelBase
from django.test import TestCase
from wiki.models import Article, ArticleRevision, URLPath, Site
from archive.models import ArchiveTransaction


# Create your tests here.
class ArchiveTestCase(TestCase):
    def setUp(self):
        ArchiveTestCase.createArticle(rev_title="root", article_type=Article, parent=None, slug=None)
        ArchiveTestCase.createArticle(rev_title="subarticle1", article_type=Article, parent=URLPath.objects.filter(slug=None)[0], slug="subarticle1")
        ArchiveTestCase.createArticle(rev_title="archive", article_type=Article, parent=URLPath.objects.filter(slug=None)[0], slug="archive")
        # todo create archive here <- implement create function in models or views

    def test_article_moved_to_archive(self):

        # get test sub article
        # article_id = URLPath.objects.filter(slug='subarticle1').values_list('article')[0]
        article = URLPath.objects.get(slug='subarticle1').article
        # article = Article.objects.get(pk=article_id)

        # get parent of test article
        parent = URLPath.objects.get(slug='subarticle1').parent.article
        # parent = Article.objects.get(pk=parent_id[0])

        # get root
        root = URLPath.objects.get(slug=None).article
        # root = Article.objects.get(pk=root_id[0])

        # parent of sub article should be root
        self.assertTrue(parent == root, "article 'parent' should be the root")

        # get archive
        archive_path = URLPath.objects.get(slug='archive')
        archive = archive_path.article

        # archive article
        transaction = ArchiveTransaction.create(archive_path)
        transaction.archive(URLPath.objects.get(slug='subarticle1'))

        parent = URLPath.objects.get(slug='subarticle1').parent.article

        # parent of sub article should be archive
        self.assertTrue(parent == archive, "article 'archive' should be the parent")



    @classmethod
    def createArticle(cls, article_type, rev_title, parent, slug):
        revision_kwargs = {'content': 'content', 'user_message': 'Crawler input', 'ip_address': 'None'}

        site = Site.objects.get_current()

        article_kwargs = {}
        # article_cls = ModelBase(article_type, (), {})
        article = article_type(**article_kwargs)
        # test = Article(**article_kwargs)
        article.add_revision(ArticleRevision(title=rev_title, **revision_kwargs),
                             save=True)
        article.save()
        newpath = URLPath.objects.create(
            site=site,
            parent=parent,
            slug=slug,
            article=article)

        article.add_object_relation(newpath)
