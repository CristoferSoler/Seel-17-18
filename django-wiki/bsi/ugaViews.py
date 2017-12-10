from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wiki.models import URLPath, Article,Site

def overviewUGA(request):
    #get all uga
    # todo get children articles of uga and give it to renderer

    uga = URLPath.get_by_path('uga/')
    children = uga.get_children()

    return render(request,'uga/overviewUGA.html',{'articles':children})