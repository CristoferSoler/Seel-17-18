import os
import django
import json
# import psycopg2
# from config import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from wiki.models import Article, URLPath, Site, ArticleRevision
from bsiwiki import settings


# from website import model

def BSI_db_import(folder_location):
    BSI_description = []
    file_description = []

    for dirpath, dirnames, filenames in os.walk(settings.CRAWLER_DIRECTORY):
        for filename in [f for f in filenames if f.endswith(".json")]:
            # get the drive and the filepath
            # drive, path_and_file = os.path.splitdrive(os.path.join(dirpath, filename))
            path_and_file = os.path.join(dirpath, filename)
            # get the path and file name
            location, file = os.path.split(path_and_file)
            # get the type of the file
            # if os.path.basename(location) == "C_MEASURE":
            #     article_type = 'CM'
            # elif os.path.basename(location) == "COMPONENT":
            #     article_type = 'C'
            # elif os.path.basename(location) == "THREAT":
            #     article_type = 'T'
            if filename.startswith("B"):
                article_type = 'C'
            else:
                article_type = 'C'
                # else:  action_type = 'G'
                # get the file id and the titel
            file_name = os.path.splitext(file)[0]
            id = " ".join(file_name.split(" ", 2)[:2])
            titel = file_name.split(" ", 2)[2]

            file_description = [id, titel, path_and_file, article_type]
            BSI_description = BSI_description + [file_description]

    return BSI_description


def insert_BSI_db():
    # BSI_description = BSI_db_import(r'C:\Users\Peter\projects\Seel-17-18\programming\bsiCrawler\content')

    for dirpath, dirnames, filenames in os.walk(settings.CRAWLER_DIRECTORY):
        for filename in [f for f in filenames if f.endswith(".json")]:
            # get the drive and the filepath
            # drive, path_and_file = os.path.splitdrive(os.path.join(dirpath, filename))
            path_and_file = os.path.join(dirpath, filename)
            # get the path and file name
            location, file = os.path.split(path_and_file)
            # get the type of the file
            # if os.path.basename(location) == "C_MEASURE":
            #     article_type = 'CM'
            # elif os.path.basename(location) == "COMPONENT":
            #     article_type = 'C'
            # elif os.path.basename(location) == "THREAT":
            #     article_type = 'T'
            # if filename.startswith("B"):
            #     article_type = 'C'
            # else:
            #     article_type = 'C'
                # else:  action_type = 'G'
                # get the file id and the titel
            file_name = os.path.splitext(file)[0]
            id = "".join(file_name.split(" ", 2)[:2])
           # title = file_name.split(" ", 2)[2]

            # read json file content in variable
            with open(path_and_file) as data_file:
                content = json.load(data_file)


            revision_kwargs = {'content': content, 'user_message': 'Crawler input', 'ip_address': 'None'}
            parent = URLPath.objects.filter(slug=None)[0]
            slug = id

            site = Site.objects.get_current()
            create_article_with_revision(site=site, parent=parent, slug=id, content=content, rev_title=file_name, rev_kwargs=revision_kwargs)


def create_article_with_revision(site, parent, slug, content, rev_title, rev_kwargs):
    article_kwargs = {}
    article = Article(**article_kwargs)
    article.add_revision(ArticleRevision(title=rev_title, **rev_kwargs),
                         save=True)
    article.save()
    newpath = URLPath.objects.create(
        site=site,
        parent=parent,
        slug=slug,
        article=article)
    article.add_object_relation(newpath)
    if not slug:
        slug = '/'
    print('Created article at ', slug)

if __name__ == '__main__':

    # Article.objects.all().delete() # thats horribly slow
    root_kwargs = {'content': '', 'user_message': 'Crawler input', 'ip_address': 'None'}
    create_article_with_revision(site = Site.objects.get_current(),parent=None, slug=None, content='', rev_title='Root', rev_kwargs=root_kwargs)
    insert_BSI_db()
    # finally:
#     conn.close()