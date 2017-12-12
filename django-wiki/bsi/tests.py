from django.test import TestCase
from wiki.models import URLPath

from .models import BSI, UGA


class BsiTestCase(TestCase):
    def setUp(self):
        rev_kwargs = {'content': '', 'user_message': 'BsiTestCase.setUp', 'ip_address': 'None'}

        # create skeleton
        root = URLPath.create_root(title='root', **rev_kwargs)
        bsi = URLPath.create_urlpath(parent=root, slug='bsi', title='bsi', **rev_kwargs)
        uga = URLPath.create_urlpath(parent=root, slug='uga', title='uga', **rev_kwargs)

        # create bsi and uga article
        BSI.create(parent=bsi, slug='bsi_article_0', title='Article 0', **rev_kwargs)
        UGA.create(parent=uga, slug='uga_article_0', title='Article 0', **rev_kwargs)

    def test_add_link_to_bsi(self):
        bsi_path = URLPath.objects.get(slug='bsi_article_0')
        bsi = BSI.objects.get(urlpath=bsi_path)

        uga_path = URLPath.objects.get(slug='uga_article_0')
        uga = UGA.objects.get(urlpath=uga_path)
        uga.add_link_to_bsi(bsi)

        self.assertEquals(bsi, uga.is_linked_to.get(urlpath=bsi_path))

    def test_remove_link_from_bsi(self):
        bsi_path = URLPath.objects.get(slug='bsi_article_0')
        bsi = BSI.objects.get(urlpath=bsi_path)

        uga_path = URLPath.objects.get(slug='uga_article_0')
        uga = UGA.objects.get(urlpath=uga_path)
        uga.add_link_to_bsi(bsi)

        self.assertEquals(bsi, uga.is_linked_to.get(urlpath=bsi_path))

        uga.remove_link_from_bsi(bsi)

        self.assertFalse(uga.is_linked_to.filter(urlpath=bsi_path))
