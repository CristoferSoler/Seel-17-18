from django.urls import reverse, resolve

from bsi.tests.super_test_case import InitTestCase


class UrlsTestCase(InitTestCase):
    def setUp(self):
        super(UrlsTestCase, self).setUp()

    def test_reverse_get_article(self):
        root = reverse('get_article', kwargs={"path": ""})
        self.assertEqual(root, '/')

        bsi = reverse('get_article', kwargs={"path": "bsi"})
        self.assertEqual(bsi, '/bsi')

        uga = reverse('get_article', kwargs={"path": "uga"})
        self.assertEqual(uga, '/uga')

    def test_resolve_get_article(self):
        bsi_resolver = resolve('/bsi')
        self.assertEqual(bsi_resolver.view_name, 'get_article')

        uga_resolver = resolve('/uga')
        self.assertEqual(uga_resolver.view_name, 'get_article')
