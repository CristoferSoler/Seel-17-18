from datetime import datetime, timedelta
import time
import sys
from sched import scheduler
from .bsiImporter import doUpdate, post_phase, doImport
from .treeview_importer import addLinksToTreeView

sys.path.append(r'../../')

#from programming.bsiCrawler.main import crawlTranslateTreeview
#from programming.bsiWizard.topicGeneration import topicGeneration
from programming.bsiComparator.bsicomparator import compare


def update_phase():
    now = datetime.now()
    archive_date = str(now.year) + '-' + str(now.month)
    delay = timedelta(days=30).total_seconds()

    print('Entering mid-phase on:', now)
    print('Post-phase will be executed on:', (now+delay).time)

    # call crawler + translator + treeview generation
    #crawlTranslateTreeview()

    # call topic generation for the wizard
    #topicGeneration()

    # call comparator
    file = compare()

    # call treeview importer
    addLinksToTreeView()

    # enter mid phase
    doUpdate(file)

    # wait 30 days and then execute post phase
    s = scheduler(time.time, time.sleep)
    s.enter(delay, 1, post_phase, archive_date)
    s.run()
    print('Post-phase has been executed.')


def demo_mid_phase():
    # for the demo we don't call crawlers and co
    doUpdate('/home/ziik/Seel-17-18/programming/bsiComparator/example_modified_files.txt')


def demo_post_phase():
    post_phase(datetime.now().strftime("%Y-%m-%d") , '/home/ziik/Seel-17-18/programming/bsiComparator/example_modified_files.txt')


if __name__ == "__main__":
    doImport()
