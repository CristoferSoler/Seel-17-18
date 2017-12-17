from wiki.models import URLPath

from bsi.models import BSI, BSI_Article_type
from bsi.tests.super_test_case import InitTestCase


class BSITestCase(InitTestCase):
    def setUp(self):
        super(BSITestCase, self).setUp()

    def test_get_or_create_bsi_root(self):
        roots = URLPath.objects.filter(slug='bsi').count()
        self.assertTrue(roots == 1, "There should be only one BSI root")
        BSI.get_or_create_bsi_root(content='')

        roots = URLPath.objects.filter(slug='bsi').count()
        self.assertTrue(roots == 1, "There should be only one BSI root")

    def test_get_or_create_bsi_subroots(self):
        BSI.get_or_create_bsi_subroots('components', 'usermsg', 'content', 'BSI Components')
        comproots = URLPath.objects.filter(slug='components').count()
        self.assertTrue(comproots == 1, "There should be only one BSI Components root")

        BSI.get_or_create_bsi_subroots('components', 'usermsg', 'content', 'BSI Components')
        comproots = URLPath.objects.filter(slug='components').count()
        self.assertTrue(comproots == 1, "There should be only one BSI Components root")

    def test_get_articles_by_type(self):
        count = len(BSI.get_articles_by_type(BSI_Article_type.COMPONENT))
        self.assertTrue(count == 1, "There should be only one BSI Component article")

        count = len(BSI.get_articles_by_type(BSI_Article_type.IMPLEMENTATIONNOTES))
        self.assertTrue(count == 0, "There should be no BSI Impl Notes article")

        count = len(BSI.get_articles_by_type(BSI_Article_type.THREAT))
        self.assertTrue(count == 0, "There should be no BSI Threat article")
