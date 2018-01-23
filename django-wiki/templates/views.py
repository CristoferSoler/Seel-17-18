from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, Http404


def banUsers(request):
    return render(request, 'admin/banUsers.html')

def assignUsers(request):
    return render(request, 'admin/assignUsers.html')
