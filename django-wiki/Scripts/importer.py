import os
import django
# import psycopg2
# from config import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsi.settings")
django.setup()
# from website import model
from bsi.models import BSIArticle

def BSI_db_import(folder_location):
    BSI_description = []
    file_description = []

    for dirpath, dirnames, filenames in os.walk(r'C:\Users\Peter\projects\Seel-17-18\programming\bsiCrawler\content'):
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
    BSI_description = BSI_db_import(r'C:\Users\Peter\projects\Seel-17-18\programming\bsiCrawler\content')

    for i in range(0, BSI_description.__len__()):
        id = BSI_description[i][0]
        title = BSI_description[i][1]
        location = BSI_description[i][2]
        article_type = BSI_description[i][3]
        BSIArticle.objects.create(id=id, title=title, location=location, article_type=article_type)


if __name__ == '__main__':
    BSIArticle.objects.all().delete()
    insert_BSI_db()
    # finally:
#     conn.close()