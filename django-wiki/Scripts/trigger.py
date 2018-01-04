from datetime import datetime, timedelta
import time
from sched import scheduler
from bsiImporter import doUpdate, post_phase


if __name__ == "__main__":
    doUpdate('../../programming/bsiComparator/example_modified_files.txt')
    scheduler = scheduler(time.time, time.sleep)
    now = datetime.now()
    archive_date = str(now.year) + '-' + str(now.month)

    print('Entering mid-phase at: ', now)
    delay = timedelta(days=30).total_seconds()
    scheduler.enter(delay, 1, post_phase, archive_date)
    scheduler.run()
    print('Post-phase has been executed.')
