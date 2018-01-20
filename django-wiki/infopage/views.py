from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, Http404
from .forms import QuestionForm, AnswerForm
from .models import Question, PageType
from wiki.models import URLPath


def information(request):
    q_form = QuestionForm()
    a_form = AnswerForm()
    if request.method == 'POST':
        if 'question_button' in request.POST:
            q_form = QuestionForm(request.POST, prefix='question')
            #pdb.set_trace()
            if q_form.is_valid():
                Question.create_question(q_form.cleaned_data['question'], request.user, PageType.INFO_PAGE)
        elif 'answer_button' in request.POST:
            a_form = AnswerForm(request.POST, prefix='answer')
            if a_form.is_valid():
                q = Question.get_question(a_form.cleaned_data['question3'])
                q.add_answer(a_form.cleaned_data['answer'], request.user)

    
    return render(request, 'info.html', {'q_form': q_form, 'a_form': a_form, 'questions': Question.get_questions(PageType.INFO_PAGE)})


def post_question(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            Question.create_question(form.cleaned_data['question'], request.user, PageType.INFO_PAGE)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()
    return render(request, 'info.html', {'form_question': form, 'questions': Question.get_questions(PageType.INFO_PAGE)})


def post_answer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            q = Question.get_question(form.cleaned_data['question'])
            q.add_answer(form.cleaned_data['answer'], request.user)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnswerForm()
    return render(request, 'info.html', {'form_answer': form, 'questions': Question.get_questions(PageType.INFO_PAGE)})
