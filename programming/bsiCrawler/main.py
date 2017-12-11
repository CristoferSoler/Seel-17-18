from scrapy import cmdline
import os
from multiprocessing import Pool
import time
from threading import Thread
from translatorMultiProcessing import checkStatus, translate


if __name__ == "__main__":

    directoryC = './md/C'
    directoryT = './md/T'
    directoryN = './md/N'

    if not os.path.exists('./md'):
        os.makedirs('./md')

    if not os.path.exists(directoryC):
        os.makedirs(directoryC)

    if not os.path.exists(directoryT):
        os.makedirs(directoryT)

    if not os.path.exists(directoryN):
        os.makedirs(directoryN)
    #
    #cmdline.execute("scrapy runspider crawli.py --nolog".split())
    files = os.listdir(directoryC)
    files.extend(os.listdir(directoryT))
    files.extend(os.listdir(directoryN))
    print(files)
    # add progressbar
    start = time.time()
    print("MultiProcessing: ", time.time() - start)
    t = Thread(target=checkStatus, args=(len(files),))
    t.start()

    # start Multiprocessing
    start = time.time()
    pool = Pool()
    pool.map(translate, files)
    fertig = True
    t.join()
    print('Finished')