from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, Http404
from .forms import QuestionForm, AnswerForm
from .models import Question
from wiki.models import URLPath

def information(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            url = URLPath.objects.get(slug='information_page')
            q = Question.create_question(form.cleaned_data['question'], request.user, url)
            return render(request, 'info.html', {'form': form, 'question': q})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'info.html', {'form': form})
