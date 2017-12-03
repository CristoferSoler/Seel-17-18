from django.db.models.base import ModelBase
from django.test import TestCase
from wiki.models import Article, ArticleRevision, URLPath, Site
from archive.models import Archive, ArchiveTransaction


class ArchiveTestCase(TestCase):
    """
    In this test case a root, a normal article and an archive are created. The test creates a transaction that puts the normal article into the archive.
    The test fails if the parent of the normal article is not the archive in the end.
    """

    def setUp(self):
        rev_kwargs = {'content': '', 'user_message': 'ArchiveTestCase.setUp', 'ip_address': 'None'}
        root = URLPath.create_urlpath(parent=None, slug=None, title='root', **rev_kwargs)
        URLPath.create_urlpath(parent=root, slug='subarticle1', title='subarticle1', **rev_kwargs)
        Archive.get_or_create(slug='2017')

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
        archive = Archive.get_archive_by_slug(slug='2017')

        # archive article
        transaction = ArchiveTransaction.create(archive)
        transaction.archive(URLPath.objects.get(slug='subarticle1'))

        parent = URLPath.objects.get(slug='subarticle1').parent

        # parent of sub article should be archive
        self.assertTrue(parent == archive.archive_url, "article '2017' should be the parent")

    def test_get_or_create_archive(self):
        number_of_urls = URLPath.objects.filter(slug='2017').count()
        self.assertTrue(number_of_urls == 1, "There should be only one archive")

        # get the same archive again
        Archive.get_or_create(slug='2017')

        # still there should be only one archive
        number_of_urls = URLPath.objects.filter(slug='2017').count()
        self.assertTrue(number_of_urls == 1, "There should be only one archive")