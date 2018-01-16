from django.db import models
from datetime import datetime, timedelta
from wiki.models import URLPath, transaction
from django.contrib.auth.models import User


def get_timestamp_now():
    return datetime.now()


class Question(models.Model):
    question = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=get_timestamp_now)
    url = models.ForeignKey(URLPath, on_delete=models.CASCADE)

    @classmethod
    def delete_old_questions():
        Question.objects.filter(timestamp__lte=datetime.now()-timedelta(days=30)).delete()

    @transaction.atomic
    @classmethod
    def create_question(text, user, url):
        q = Question(question=text, user=user, url=url)
        q.save()

    @classmethod
    def get_questions(url):
        return Question.objects.filter(url=url)

    def add_answer(self, text, user):
        return self.answer_set.create(answer=text, user=user)

    def delete_question(self):
        # TODO
        pass

    def edit_question(self, text):
        # TODO
        pass

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=get_timestamp_now)

    def edit_answer(self, text):
        # TODO
        pass
