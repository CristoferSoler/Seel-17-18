import os
import django
import win32com.client

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from wiki.models import Article, URLPath, Site, ArticleRevision
from bsiwiki import settings
from bsi.models import BSI, UGA

#rootparent = URLPath.objects.filter(slug=None)[0]#root
#site = Site.objects.get_current()

# root article exists already
#slug = 'uga1'
#article2_kwargs = {}
#article2 = Article(**article2_kwargs)
#rev_kwargs2 = {'content': 'this is uga article 1', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'}
#rev2 = ArticleRevision(title='uga article1 title', **rev_kwargs2)
#article2.add_revision(rev2, save=True)
#article2.save()

#newpath = URLPath.objects.create(
#        site=site,
#        parent=rootparent,
#        slug=slug,
#        article=article2)
#article2.add_object_relation(newpath)

#ugaArt = UGA(article=article2)
#ugaArt.save()

#root
rootparent = URLPath.objects.filter(slug=None)[0]#root
site = Site.objects.get_current()

#root/bsi
slug = 'bsi';
article_kwargs = {};
article = Article(**article_kwargs);
rev_kwargs = {'content': 'this is bsi', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'};
rev = ArticleRevision(title='BSI Catalog', **rev_kwargs);
article.add_revision(rev, save=True);
article.save();

newpath = URLPath.objects.create(
        site=site,
        parent=rootparent,
        slug=slug,
        article=article)
article.add_object_relation(newpath)

bsiparent = URLPath.objects.filter(slug='bsi')[0]

#roots/bsi/components
slug = 'components';
article1_kwargs = {};
article1 = Article(**article1_kwargs);
rev1_kwargs = {'content': 'this is components', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'};
rev1 = ArticleRevision(title='Components', **rev1_kwargs);
article1.add_revision(rev1, save=True);
article1.save();

newpath = URLPath.objects.create(
        site=site,
        parent=bsiparent,
        slug=slug,
        article=article1)
article1.add_object_relation(newpath)

#roots/bsi/threats
slug = 'threats';
article2_kwargs = {};
article2 = Article(**article2_kwargs);
rev2_kwargs = {'content': 'this is threats', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'};
rev2 = ArticleRevision(title='Threats', **rev2_kwargs);
article2.add_revision(rev2, save=True);
article2.save();

newpath = URLPath.objects.create(
        site=site,
        parent=bsiparent,
        slug=slug,
        article=article2)
article2.add_object_relation(newpath)

# roots/bsi/countermeasures
slug = 'countermeasures';
article3_kwargs = {};
article3 = Article(**article3_kwargs);
rev3_kwargs = {'content': 'this is countermeasures', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'};
rev3 = ArticleRevision(title='CounterMeasures', **rev3_kwargs);
article3.add_revision(rev3, save=True);
article3.save();

newpath = URLPath.objects.create(
        site=site,
        parent=bsiparent,
        slug=slug,
        article=article3)
article3.add_object_relation(newpath)

#testing one countermeasure
# roots/bsi/countermeasures/M2.4231
site = Site.objects.get_current()
parent = URLPath.objects.filter(slug='countermeasures')[0]
slug = 'M2.4231';
article4_kwargs = {};
article4 = Article(**article4_kwargs);
rev4_kwargs = {'content': 'this is one countermeasure M2.4231', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'};
rev4 = ArticleRevision(title='M2.4231', **rev4_kwargs);
article4.add_revision(rev4, save=True);
article4.save();

newpath = URLPath.objects.create(
        site=site,
        parent=parent,
        slug=slug,
        article=article4)
article4.add_object_relation(newpath)
bsiArt = BSI(article=article4, bsi_id='M2.4231')
bsiArt.save()
#bsiArt.references.add(ugaArt)
