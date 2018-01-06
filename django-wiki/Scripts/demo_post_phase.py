from bsiImporter import after_midphase
from sched import scheduler
import time

def postPhase():
    scheduler = scheduler(time.time, time.sleep)
    print('Entering post-phase...')
    scheduler.enter(0, 1, after_midphase, ())
    scheduler.run()
