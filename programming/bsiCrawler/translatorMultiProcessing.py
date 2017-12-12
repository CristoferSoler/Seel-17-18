from googletrans import Translator
import os
import re
import time
import progressbar
import functools

def content_from_list(content):
    mdFilePart = ''
    for den in content:
        if (not isinstance(den, list)):
            mdFilePart += den + '\n\n'
        else:
            for li in den:
                mdFilePart += '* ' + li + '\n'
            mdFilePart += '\n\n'
    return mdFilePart + '\n\n'

urls = [
        'translate.google.com',
        'translate.google.co.kr',
        'translate.google.de',
        'translate.google.at',
        'translate.google.pl',
        'translate.google.am',
        'translate.google.ba',
        'translate.google.ae',
        'translate.google.ad',
        'translate.google.be',
        'translate.google.bf',
        'translate.google.bg',
        'translate.google.ba',
        'translate.google.bi',
        'translate.google.bj',
        'translate.google.bs',
        'translate.google.by',
        'translate.google.cm',
        'translate.google.cn',
        'translate.google.ca',
        'translate.google.cv',
        'translate.google.fr',
        'translate.google.fm',
        'translate.google.ga',
        'translate.google.ge',
        'translate.google.gg',
        'translate.google.gl',
        'translate.google.es',
        'translate.google.gy',
        'translate.google.gr',
        'translate.google.gp',
        'translate.google.gp',
        'translate.google.hr',
        'translate.google.ht',
        'translate.google.hu',]

directoryContentEN = './contentEn/'
directoryContent = './content/'
directoryC = './md/C'
directoryN = './md/N'
directoryT = './md/T'
directoryEN = './mdEn'
fertig = False

def checkStatus(filesLenght):
    bar = progressbar.ProgressBar(maxval=filesLenght).start()
    files = os.listdir(directoryEN)
    lastFile = len(files)
    while (fertig != True):

        filesC = os.listdir(directoryC)
        filesN = os.listdir(directoryN)
        filesT = os.listdir(directoryT)

        lenFiles = len(filesC) + len(filesN) + len(filesT)
        if(lastFile != lenFiles):
            bar.update(lenFiles)
            lastFile = lenFiles
        else:
            pass
        time.sleep(0.1)

    bar.finish()
    return


def check15k(list):
    listOf15k = []
    splitList = list.splitlines()
    listOf15kElement = []

    for line in splitList:
        if((functools.reduce(lambda x,y: x+y,map(len, listOf15kElement),0)+ len(line))< 3999):
            listOf15kElement.append(line)

        else:
            listOf15k.append('\n'.join(listOf15kElement))

            listOf15kElement = [line]

    listOf15k.append('\n'.join(listOf15kElement))

    return listOf15k


def translate(fileMD):
    translator = Translator(service_urls=urls)

    filename = os.fsdecode(fileMD)
    dir = ''
    filenameEn = translator.translate(filename, dest='en', src='de').text

    try:
        f = open(directoryC + '/' + fileMD)
        dir += 'C/'
    except:
        try:
            f = open(directoryN + '/' + fileMD)
            dir += 'N/'
        except:
            f = open(directoryT + '/' + fileMD)
            dir += 'T/'

    contentOfMdDE = f.read()
    listOf15k = check15k(contentOfMdDE)
    textEl = ''
    for el in listOf15k:
        textEl += translator.translate(el, dest='en', src='de').text

    f = open(directoryEN + '/' + dir + re.sub('/', '-', filenameEn),'w', encoding='utf-8' )
    f.write(textEl)
    f.close()
