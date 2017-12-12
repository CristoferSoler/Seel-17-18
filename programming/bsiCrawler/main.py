from multiprocessing import Pool
from threading import Thread
from translatorMultiProcessing import checkStatus, translate
import os, shutil
import time

'''
This module is the main module for retrieving data from the BSI. It generates all necessary folder structures, 
retrieves the content from the BSI and translates it into English.
'''

def deleteAllFilesInDirectory(directory):
    for the_file in os.listdir(directory):
        file_path = os.path.join(directory, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def main():
    #directorys to store the content of the bsi
    directoryC = './md/C'
    directoryT = './md/T'
    directoryN = './md/N'

    print('Getting Started with Data from the BSI')
    print('Delete all Files of the md directory')
    deleteAllFilesInDirectory('./md')
    deleteAllFilesInDirectory('./mdEn')
    print('Deleting is is completed')

    print('Missing folder structures are created.')
    if not os.path.exists('./md'):
        os.makedirs('./md')

    if not os.path.exists('./mdEn'):
        os.makedirs('./mdEn')

    if not os.path.exists('./mdEn/C'):
        os.makedirs('./mdEn/C')

    if not os.path.exists('./mdEn/N'):
        os.makedirs('./mdEn/N')

    if not os.path.exists('./mdEn/T'):
        os.makedirs('./mdEn/T')

    if not os.path.exists('./treeview'):
        os.makedirs('./treeview')

    if not os.path.exists(directoryC):
        os.makedirs(directoryC)

    if not os.path.exists(directoryT):
        os.makedirs(directoryT)

    if not os.path.exists(directoryN):
        os.makedirs(directoryN)

    print('Missing folder structures have been created.')

    os.system("scrapy runspider crawli.py --nolog")

    #start translation with Multiprocessing
    print('Start the translation')
    files = os.listdir(directoryC)
    files.extend(os.listdir(directoryT))
    files.extend(os.listdir(directoryN))

    pool = Pool()
    pool.map(translate, files)
    print('Translation is finished')

    print('Generate treeview of the BSI')
    os.system("scrapy runspider crawliTree.py --nolog")
    print('Generation of the treeview is finshed')

if __name__ == "__main__":
    main()
