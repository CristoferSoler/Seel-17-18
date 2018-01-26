from django.http import HttpResponse
import json

def getTreeview(request):
    with open('/home/ziik/Seel-17-18/programming/bsiCrawler/treeview/bsiTreeLinks.txt') as f:
       jsonFile = f.read()
       print(jsonFile)
       return HttpResponse(jsonFile, content_type='application/json')
