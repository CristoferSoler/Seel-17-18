import sys
from os import environ
import django


sys.path.append(r'..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()


from infopage.models import Question


def main():
    Question.delete_old_questions()


if __name__ == '__main__':
    main()
