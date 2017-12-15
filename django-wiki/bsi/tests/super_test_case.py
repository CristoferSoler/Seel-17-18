from django.test import TestCase
from wiki.models import URLPath

from bsi.models import BSI, UGA, BSI_Article_type


class BsiTestCase(TestCase):
    def setUp(self):
        rev_kwargs = {'content': '', 'user_message': 'BsiTestCase.setUp', 'ip_address': 'None'}

        # create skeleton
        root = URLPath.create_root(title='root', **rev_kwargs)
        bsi = URLPath.create_urlpath(parent=root, slug='bsi', title='bsi', **rev_kwargs)
        uga = URLPath.create_urlpath(parent=root, slug='uga', title='uga', **rev_kwargs)

        # create bsi and uga article
        BSI.create(parent=bsi, article_type=BSI_Article_type.COMPONENT, slug='bsi_article_0', title='Article 0', **rev_kwargs)
        UGA.create(parent=uga, slug='uga_article_0', title='Article 0', **rev_kwargs)
