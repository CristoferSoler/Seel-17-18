import sys
from os import environ
import django
from datetime import timedelta


sys.path.append(r'..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()


from infopage.models import Question, get_timestamp_now
from django.contrib.auth.models import User


def main():
    delete_old_q()
    delete_unvalidated_users()


def delete_old_q():
    Question.delete_old_questions()


def delete_unvalidated_users():
    User.objects.filter(last_login=None, date_joined__lte=get_timestamp_now()-timedelta(day=1)).delete()


if __name__ == '__main__':
    main()
