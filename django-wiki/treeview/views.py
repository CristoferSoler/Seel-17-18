from django.http import HttpResponse
import json
from bsiwiki import settings

def getTreeview(request):
    with open(settings.BSI_TREE_LINKS) as f:
       jsonFile = f.read()
       print(jsonFile)
       return HttpResponse(jsonFile, content_type='application/json')
