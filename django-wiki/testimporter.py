import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from wiki.models import Article, URLPath, Site, ArticleRevision
from bsiwiki import settings
from bsi.models import BSI, UGA

parent = URLPath.objects.filter(slug=None)[0]
site = Site.objects.get_current()

# root article exists already
slug = 'uga1'
article2_kwargs = {}
article2 = Article(**article2_kwargs)
rev_kwargs2 = {'content': 'this is uga article 1', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'}
rev2 = ArticleRevision(title='uga article1 title', **rev_kwargs2)
article2.add_revision(rev2, save=True)
article2.save()

newpath = URLPath.objects.create(
        site=site,
        parent=parent,
        slug=slug,
        article=article2)
article2.add_object_relation(newpath)

ugaArt = UGA(article=article2)
ugaArt.save()



slug = 'bsi1';
article_kwargs = {};
article = Article(**article_kwargs);
rev_kwargs = {'content': 'this is bsi article 1', 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'};
rev = ArticleRevision(title='bsi article1 title', **rev_kwargs);
article.add_revision(rev, save=True);
article.save();

newpath = URLPath.objects.create(
        site=site,
        parent=parent,
        slug=slug,
        article=article)
article.add_object_relation(newpath)

bsiArt = BSI(article=article, bsi_id='b1.1.1')
bsiArt.save()
bsiArt.references.add(ugaArt)

