import os
import django
import json

# import psycopg2
# from config import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from wiki.models import Article, URLPath, Site, ArticleRevision
from bsiwiki import settings
from bsi.models import BSI, UGA
import bsi_sitemap as parent_bsi
from wiki.core.markdown import article_markdown

# import the BSI articles to the database "first import"
def insert_BSI_db():
    site = Site.objects.get_current()
    for dirpath, dirnames, filenames in os.walk(settings.CRAWLER_DIRECTORY):
        for filename in [f for f in filenames if f.endswith(".md")]:
            # get the drive and the filepath
            path_and_file = os.path.join(dirpath, filename)
            # get the path and file name
            location, file = os.path.split(path_and_file)
            # get the file id and the titel
            file_name = os.path.splitext(file)[0]
            id = "".join(file_name.split(" ", 2)[:2])
            # read md file content in variable
            with open(path_and_file) as data_file:
                content = data_file.readlines()
                revision_kwargs = {'content': content, 'user_message': 'Crawler input', 'ip_address': '0.0.0.0'}
                parent = parent_bsi.checkType(id) #example.com/root/bsi/components or threats or counterMeasures
                create_article_with_revision(site=site, parent=parent, slug= id, content=content, rev_title=file_name, rev_kwargs=revision_kwargs)

# generate article
def create_article_with_revision(site, parent, slug, content, rev_title, rev_kwargs):
    article_kwargs = {}
    article = Article(**article_kwargs)
    article.add_revision(ArticleRevision(title=rev_title, **rev_kwargs), save=True)
    article.save()
    newpath = URLPath.objects.create(
        site=site,
        parent=parent,
        slug=slug,
        article=article)
    article.add_object_relation(newpath)
    bsiArt = BSI(article=article, bsi_id=slug)
    bsiArt.save()
    if not slug:
        slug = '/'
    print('Created article at ', slug)

if __name__ == '__main__':

    insert_BSI_db()
    #finally:
#     conn.close()