from django.db import models
from datetime import timedelta
from wiki.models import transaction
from django.contrib.auth.models import User
from django.utils import timezone
from enumfields import Enum, EnumField


class PageType(Enum):
    FAQ = 'FAQ'
    INFO_PAGE = 'INFO_PAGE'

    class Labels:
        FAQ = 'Frequently Asked Questions'
        INFO_PAGE = 'Information Page'


def get_timestamp_now():
    # this sets the TZ to utc by default
    return timezone.now()


class Question(models.Model):
    question = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=get_timestamp_now)
    url = EnumField(PageType)

    @classmethod
    def delete_old_questions(cls):
        cls.objects.filter(timestamp__lte=timezone.now()-timedelta(days=30)).delete()

    @classmethod
    @transaction.atomic
    def create_question(cls, text, user, url):
        q = cls(question=text, user=user, url=url)
        q.save()
        return q

    @classmethod
    def get_questions(cls, url):
        return cls.objects.filter(url=url)

    @classmethod
    def get_question(cls, q_id):
        try:
            return Question.objects.get(id=q_id)
        except Exception:
            return None

    def add_answer(self, text, user):
        return self.answer_set.create(answer=text, user=user)

    def delete_question(self):
        self.delete()

    @transaction.atomic
    def edit_question(self, text):
        self.question = text
        self.save()

    def get_answers(self):
        return self.answer_set.all()

    def __str__(self):
        return 'Question: ' + self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=get_timestamp_now)

    @transaction.atomic
    def edit_answer(self, text):
        self.answer = text
        self.save()

    def __str__(self):
        return 'Answer: ' + self.answer
