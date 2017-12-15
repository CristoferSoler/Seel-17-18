from django.test import TestCase
from wiki.models import URLPath

from bsi.models import BSI, UGA
from bsi.tests.super_test_case import BsiTestCase
from bsi.tests.urls import UrlsTestCase


class UGATestCase(BsiTestCase):
    def setUp(self):
        super(UGATestCase, self).setUp()

    def test_add_link_to_bsi(self):
        bsi_path = URLPath.objects.get(slug='bsi_article_0')
        bsi = BSI.objects.get(url=bsi_path)

        uga_path = URLPath.objects.get(slug='uga_article_0')
        uga = UGA.objects.get(url=uga_path)
        uga.add_link_to_bsi(bsi)

        self.assertEquals(bsi, uga.is_linked_to.get(url=bsi_path))

    def test_remove_link_from_bsi(self):
        bsi_path = URLPath.objects.get(slug='bsi_article_0')
        bsi = BSI.objects.get(url=bsi_path)

        uga_path = URLPath.objects.get(slug='uga_article_0')
        uga = UGA.objects.get(url=uga_path)
        uga.add_link_to_bsi(bsi)

        self.assertEquals(bsi, uga.is_linked_to.get(url=bsi_path))

        uga.remove_link_from_bsi(bsi)

        self.assertFalse(uga.is_linked_to.filter(url=bsi_path))
