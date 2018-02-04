from django.test import TestCase
from datetime import timedelta
from django.contrib.auth.models import User
from wiki.models import URLPath
from infopage.models import Question, Answer
from django.utils import timezone


class InitTestCase(TestCase):
    def setUp(self):
        rev_kwargs = {'content': '', 'user_message': 'QuestionTestCase.setUp', 'ip_address': 'None'}
        root = URLPath.create_root(title='root', **rev_kwargs)
        url = URLPath.create_urlpath(parent=root, slug='informationPage', title='information page', **rev_kwargs)
        q_user = User.objects.create_user('user0', None, '1234')
        a_user = User.objects.create_user('user1', None, '1234')
        # create_question and add_answer are tested here?
        q = Question.create_question(text="How can I test your website", user=q_user, url=url)
        q.add_answer(text="you can run the test unit :)", user=a_user)


class QuestionTestCase(InitTestCase):
    def setUp(self):
        super(QuestionTestCase, self).setUp()

    def test_get_questions(self):
        url = URLPath.objects.get(slug="informationPage")
        questions = Question.get_questions(url=url).count()
        self.assertGreater(questions, 0, "There should be one or more questions")

    def test_get_answers(self):
        user = User.objects.get(username="user0")
        q = Question.objects.get(question="How can I test your website", user=user)
        answers = q.get_answers().count()
        self.assertGreater(answers, 0, "There should be one or more answers for the question")

    def test_delete_question(self):
        user = User.objects.get(username="user0")
        q = Question.objects.get(question="How can I test your website")
        q.delete_question()
        d_question = Question.objects.filter(user=user).count()
        self.assertTrue(d_question == 0, "There should be no question")
        user2 = User.objects.get(username="user1")
        count_answer = Answer.objects.filter(user=user2).count()
        self.assertTrue(count_answer == 0, "There should be no answers to the deleted question")

    def test_edit_question(self):
        q = Question.objects.get(question="How can I test your website")
        new_q = "how can I test your application"
        q.edit_question(new_q)
        self.assertEqual(q.question, new_q, "The question is modified")

    def test_delete_old_questions(self):
        user = User.objects.get(username="user0")
        q = Question.objects.filter(user=user)[0]
        q.timestamp = timezone.now() - timedelta(days=32)
        q.save()
        Question.delete_old_questions()
        count = Question.objects.filter(user=user).count()
        self.assertTrue(count == 0, "There should be no questions and answers after 30 days in the Information Page")


class AnswerTestCase(InitTestCase):
    def setUp(self):
        super(AnswerTestCase, self).setUp()

    def test_edit_answer(self):
        q = Question.objects.get(question="How can I test your website")
        answer = q.get_answers()[0]
        new_a = "same way"
        answer.edit_answer(new_a)
        self.assertEqual(answer.answer, new_a, "The answer is modified")
