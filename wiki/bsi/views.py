from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import <tableName>

def index(request):
   # <var:all_tuples_of_a_Table:Name> = <tableName>.objects.all()
    template = loader.get_template('bsi/index.html')
    context = {
    #     '<all_tuples_of_a_Table:Name>':<var:all_tuples_of_a_Table:Name>,
    }
    return HttpResponse(template.render(context, request))