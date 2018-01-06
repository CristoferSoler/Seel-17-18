from django.http import HttpResponse
import json
import sys

sys.path.append(r'..')

from Scripts.demo_mid_phase import midPhase
from Scripts.demo_post_phase import postPhase


def performMidPhase(request):
    midPhase()
    print('MidPhase')

def performPostPhase(request):
    postPhase()
    print('PostPhase')


'''
def getTreeview(request):
    with open('./../programming/bsiCrawler/treeview/bsiTreeLinks.txt') as f:
       jsonFile = f.read()
       print(jsonFile)
       return HttpResponse(jsonFile, content_type='application/json')
'''