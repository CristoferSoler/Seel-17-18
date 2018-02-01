from django.http import HttpResponse
import json
import sys
from django.contrib import messages
from django.http import Http404

sys.path.append(r'..')

from Scripts.main import update_phase, check_update_progress#,demo_mid_phase, demo_post_phase

update_done = dict(status='ok',msg='Update done!')
error_update = dict(status='error',msg='Already updated')

'''
def performMidPhase(request):
    demo_mid_phase()
    print('MidPhase')
    return HttpResponse('', content_type='application/json')

def performPostPhase(request):
    demo_post_phase()
    print('PostPhase')
    return HttpResponse('', content_type='application/json')

'''
def check_update(request):
    isRunning = check_update_progress()
    update_running = dict(status = isRunning, msg = 'Update still running')
    return HttpResponse(json.dumps(update_running), content_type='application/json')

def Update(request):
    try:
        if(update_phase()):
            return HttpResponse(json.dumps(update_done), content_type='application/json')
    except:
        return HttpResponse(json.dumps(error_update), content_type='application/json')
#
'''
def getTreeview(request):
    with open('./../programming/bsiCrawler/treeview/bsiTreeLinks.txt') as f:
       jsonFile = f.read()
       print(jsonFile)
       return HttpResponse(jsonFile, content_type='application/json')
'''