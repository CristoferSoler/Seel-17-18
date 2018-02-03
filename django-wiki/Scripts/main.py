from datetime import datetime, timedelta
import time
import sys
from sched import scheduler
import os
import django

sys.path.append(r'..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from Scripts.treeview_links import addLinksToTreeView
from Scripts.bsiImporter import doUpdate, post_phase, doImport
# from Scripts.bsiWizard.topicGeneration import topicGeneration
# from Scripts.bsiComparator.bsicomparator import compare

isRunning = False


def update_phase():
    global isRunning
    isRunning = True

    print('Entering mid-phase on:', datetime.now())

    # call crawler
    # os.system('scrapy runspider bsiCrawler/crawli.py -a phase=1 --nolog')

    # call comparator
    # compare()

    # call translator
    # os.system('python3 bsiCrawler/translatorMultiProcessing.py 1')

    # enter mid phase
    res = doUpdate()
    if res:
        return res

    try:
        # wait 30 days and then execute post phase
        delay = timedelta(minutes=1).total_seconds()
        s = scheduler(time.time, time.sleep)
        s.enter(delay, 1,  post_phase)
        s.run()
    except Exception as e:
        print(e)
        isRunning = False
        return 'An error has occurred. Update process aborted'

    # call treeview importer
    addLinksToTreeView()

    # call topic generation for the wizard
    # topicGeneration()

    print('Post-phase has been executed.')
    isRunning = False
    return ''


def check_update_progress():
    return isRunning


if __name__ == "__main__":
    # call crawler
    # os.system('scrapy runspider bsiCrawler/crawli.py -a phase=0 --nolog')

    # call translator
    # os.system('python3 bsiCrawler/translatorMultiProcessing.py 0')

    doImport()

    # call treeview importer
    addLinksToTreeView()

    # call topic generation for the wizard
    # topicGeneration()
