from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def createAricle(name,user,date):
    return {'name':name, 'user':user,'date':date}

def overviewUGA(request):
    articles = [createAricle('Test1','user1','20.1'),createAricle('Test2','user2','20.1'),createAricle('Test3','user3','20.1'),createAricle('Test4','user4','20.1'),createAricle('Test5','user5','20.1'),createAricle('Test6','user6','20.1'),createAricle('Test7','user7','20.1'),createAricle('Test8','user8','20.1'),createAricle('Test9','user9','20.1'),createAricle('Test10','user10','20.1'),createAricle('Test11','user11','20.1'),createAricle('Test1','user12','20.12'),createAricle('Test13','user13','20.1'),createAricle('Test14','user14','20.1'),createAricle('Test15','user15','20.1'),createAricle('Test16','user16','20.1'),createAricle('Test17','user17','20.1'),createAricle('Test18','user18','20.1'),createAricle('Test19','user19','20.1'),createAricle('Test20','user20','20.1'),createAricle('Test21','user21','20.1')]
    #get all uga
    # todo get children articles of uga and give it to renderer

    return render(request,'uga/overviewUGA.html',{'articles':articles})