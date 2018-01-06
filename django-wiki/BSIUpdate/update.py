from django.http import HttpResponse
import json
import sys

sys.path.append(r'..')

from Scripts.main import demo_mid_phase, demo_post_phase


def performMidPhase(request):
    demo_mid_phase()
    print('MidPhase')
    return HttpResponse('', content_type='application/json')

def performPostPhase(request):
    demo_post_phase()
    print('PostPhase')
    return HttpResponse('', content_type='application/json')


'''
def getTreeview(request):
    with open('./../programming/bsiCrawler/treeview/bsiTreeLinks.txt') as f:
       jsonFile = f.read()
       print(jsonFile)
       return HttpResponse(jsonFile, content_type='application/json')
'''