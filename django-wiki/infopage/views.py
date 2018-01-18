from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, Http404


def information(request):
    return render(request, 'info.html')
