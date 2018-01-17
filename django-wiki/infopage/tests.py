from django.test import TestCase
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from wiki.models import URLPath
from infopage.models import Question, Answer

class InitTestCase(TestCase):
    def setUp(self):
        rev_kwargs = {'content': '', 'user_message': 'QuestionTestCase.setUp', 'ip_address': 'None'}
        root = URLPath.create_root(title='root', **rev_kwargs)
        url = URLPath.create_urlpath(parent=root, slug='informationPage', title='bsi', **rev_kwargs)
        q_user = User.objects.create_user('user0', None, '1234')
        a_user = User.objects.create_user('user1', None, '1234')
        q = Question()
        q.create_question(question="How can I test your website",user=q_user,url=url)
        answer = q.add_answer(text="you can run the test unit :)", user=a_user)
        answer.save()


class QuestionTestCase(InitTestCase):
    def setUp(self):
        super(QuestionTestCase, self).setUp()

    # def test_add_answer(self):
    #     user = User.objects.get(username="user0")
    #     a_user = User.objects.get(username="user1")
    #     q = Question.objects.get(question="How can I test your website", user=user)
    #     q.answer_set.create(answer="you can run the test unit :)", user=a_user)
    #     q.save()
    #     answer = Answer.objects.filter(question=q, user=a_user).count()
    #     self.assertTrue(answer ==1, "There should be one answer")


    def test_get_questions(self):
        url = URLPath.objects.get(slug = "informationPage")
        questions = Question.objects.filter(url=url).count()
        self.assertGreater(questions, 0, "There should be one or more questions")

    def test_get_answers(self):
        user = User.objects.get(username="user0")
        q = Question.objects.get(question = "How can I test your website", user = user)
        answers = Answer.objects.filter(question=q).count()
        self.assertGreater(answers, 0, "There should be one or more answers for the question")

    def test_delete_question(self):
        user = User.objects.get(username="user0")
        q = Question.objects.get(question="How can I test your website")
        answers = q.get_answers().delete()
        answers = Answer.objects.filter(question=q).count()
        self.assertTrue( answers == 0, "There should be no answers")
        q.delete()
        d_question = Question.objects.filter(question=q.question, user =user).count()
        self.assertTrue(d_question == 0, "There should be no question")

    def test_edit_question(self):
        q = Question.objects.get(question="How can I test your website")
        new_q = "how can I test your application"
        q.question = new_q
        self.assertEqual(q.question, new_q, "The question is modified")

    def test_delete_old_questions(self):
        timpe_stamp = datetime.now()- timedelta(days=30)
        self.assertLessEqual(timpe_stamp.day, 30, "Deleting should be after 30 days")
        questions = Question.objects.filter(timestamp__lte=timpe_stamp).count()
        self.assertTrue(questions == 0, "There should be no questions and answers after 30 days in the Information Page")


class AnswerTestCase(InitTestCase):
    def setUp(self):
        super(AnswerTestCase, self).setUp()

    def test_edit_answer(self):
        q = Question.objects.get(question="How can I test your website")
        user = User.objects.get(username="user1")
        answer = Answer.objects.get(question=q)
        new_a = "same way"
        answer.answer = new_a
        self.assertEqual(answer.answer, new_a, "The answer is modified")





