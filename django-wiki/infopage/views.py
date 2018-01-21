from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuestionForm, AnswerForm
from .models import Question, PageType
from django.urls import reverse
import pdb

def information(request):
    #pdb.set_trace()
    if request.method == 'POST':
        if 'question_button' in request.POST:
            q_form = QuestionForm(request.POST)
            if q_form.is_valid():
                if(request.user.is_authenticated):
                    Question.create_question(q_form.cleaned_data['question'], PageType.INFO_PAGE, request.user)
                else:
                    Question.create_question(q_form.cleaned_data['question'], PageType.INFO_PAGE)
        elif 'answer_button' in request.POST:
            a_form = AnswerForm(request.POST)
            if a_form.is_valid():
                if(a_form.cleaned_data['answer_from']):
                    q = Question.get_question(a_form.cleaned_data['answer_from'])
                    if(request.user.is_authenticated):
                        q.add_answer(a_form.cleaned_data['answer'], request.user)
                    else:
                        q.add_answer(a_form.cleaned_data['answer'])
        q_form = QuestionForm()
        a_form = AnswerForm()
        return HttpResponseRedirect(reverse('information'))
    else:
        q_form = QuestionForm()
        a_form = AnswerForm()
        return render(request, 'info.html', {'q_form': q_form, 'a_form': a_form, 'questions': Question.get_questions(PageType.INFO_PAGE)})
