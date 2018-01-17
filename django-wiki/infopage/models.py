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
    def delete_old_questions(cls):
        cls.objects.filter(timestamp__lte=datetime.now()-timedelta(days=30)).delete()

    @transaction.atomic
    @classmethod
    def create_question(cls,text, user, url):
            q = cls(question=text,user= user,url= url)
            q.save()

    @classmethod
    def get_questions(cls,url):
        return cls.objects.filter(url=url)

    def add_answer(self, text, user):
            return  self.answer_set.create(answer=text, user=user)

    def delete_question(self):
            if(self.get_answers()):
                answers = self.get_answers().delete()
                answers.delete()
                answers.save()
            self.delete()
            self.save()


    def edit_question(self,text):
            self.question = text
            self.save()


    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=get_timestamp_now)

    def edit_answer(self, text):
            self.answer = text
            self.save()
