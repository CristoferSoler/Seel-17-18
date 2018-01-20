from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, Http404
from .forms import QuestionForm, AnswerForm
from .models import Question, PageType
from wiki.models import URLPath


def information(request):
    if request.method == 'POST':
        if 'question_button' in request.POST:
            q_form = QuestionForm(request.POST)
            if q_form.is_valid():
                Question.create_question(q_form.cleaned_data['question'], request.user, PageType.INFO_PAGE)
        elif 'answer_button' in request.POST:
            a_form = AnswerForm(request.POST)
            if a_form.is_valid():
                print(a_form.cleaned_data['question3'])
                q = Question.get_question(a_form.cleaned_data['question3'])
                q.add_answer(a_form.cleaned_data['answer'], request.user)

    q_form = QuestionForm()
    a_form = AnswerForm()
    return render(request, 'info.html', {'q_form': q_form, 'a_form': a_form, 'questions': Question.get_questions(PageType.INFO_PAGE)})
