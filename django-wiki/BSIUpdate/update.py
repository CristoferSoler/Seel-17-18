from django.http import HttpResponse
import json
import sys

sys.path.append(r'..')

from Scripts.main import update_phase, check_update_progress

update_done = dict(status='ok', msg='Update is finished!')


def check_update(request):
    isRunning = check_update_progress()
    update_running = dict(status=isRunning, msg='Update is still running...')
    return HttpResponse(json.dumps(update_running), content_type='application/json')


def update(request):
    res = update_phase()
    if not res:
            return HttpResponse(json.dumps(update_done), content_type='application/json')
    else:
        error_update = dict(status='error', msg=res)
        return HttpResponse(json.dumps(error_update), content_type='application/json')
