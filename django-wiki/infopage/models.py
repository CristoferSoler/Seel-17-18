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
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='q_edited_by')

    @classmethod
    def delete_old_questions(cls):
        cls.objects.filter(timestamp__lte=timezone.now()-timedelta(days=30)).delete()

    @classmethod
    @transaction.atomic
    def create_question(cls, text, url, user=None):
        if user:
            q = cls(question=text, user=user, url=url)
        else:
            q = cls(question=text, url=url)
        q.save()
        return q

    @classmethod
    def get_questions(cls, url):
        return cls.objects.filter(url=url).order_by('-timestamp')

    @classmethod
    def get_question(cls, q_id):
        try:
            return Question.objects.get(id=q_id)
        except Exception:
            return None

    def add_answer(self, text, user=None):
        if user:
            return self.answer_set.create(answer=text, user=user)
        else:
            return self.answer_set.create(answer=text)

    def delete_question(self):
        self.delete()

    @transaction.atomic
    def edit_question(self, text, user):
        self.question = text
        self.timestamp = get_timestamp_now()
        self.edited = True
        self.edited_by = user
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
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='a_edited_by')

    @classmethod
    def get_answer(cls, id):
        return Answer.objects.filter(id=id)[0]

    @transaction.atomic
    def edit_answer(self, text, user):
        self.answer = text
        self.timestamp = get_timestamp_now()
        self.edited = True
        self.edited_by = user
        self.save()

    def delete_answer(self):
        self.delete()

    def __str__(self):
        return 'Answer: ' + self.answer
