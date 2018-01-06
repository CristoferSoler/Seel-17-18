from datetime import datetime, timedelta
import time
import sys
from sched import scheduler
from .bsiImporter import doUpdate, post_phase

sys.path.append(r'../../')

from programming.bsiCrawler.main import crawlTranslateTreeview
from programming.bsiWizard.topicGeneration import topicGeneration

if __name__ == "__main__":

    # call crawler + translator + treeview generation
    crawlTranslateTreeview()

    #call topic generation for the wizard
    topicGeneration()

    doUpdate('../../programming/bsiComparator/example_modified_files.txt')
    scheduler = scheduler(time.time, time.sleep)
    now = datetime.now()
    archive_date = str(now.year) + '-' + str(now.month)

    print('Entering mid-phase at: ', now)
    delay = timedelta(days=30).total_seconds()
    scheduler.enter(delay, 1, post_phase, archive_date)
    scheduler.run()
    print('Post-phase has been executed.')
