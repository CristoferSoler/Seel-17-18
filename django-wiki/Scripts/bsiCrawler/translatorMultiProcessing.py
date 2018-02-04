import functools
import os
import re
import django
import sys
from googletrans import Translator
from multiprocessing import Pool


sys.path.append(r'..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()


from Scripts import bsiImporter
from bsiwiki import settings

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

def check15k(list, component):
    listOf15k = []
    splitList = list.splitlines()
    listOf15kElement = []
    referenceList = []
    ref = False
    threats = False
    text = True

    for line in splitList:
        if(component):
            if ('5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen' in line):
                threats = True
                referenceList.append(line)


            if (threats and '* ' in line):
                referenceList.append(line)

            if ('4 Weiterführende Informationen' in line):
                text = False

            if ('##' in line and '* ' not in line and '4.1 Literatur' not in line):
                referenceList.append(line)


        if(text and (functools.reduce(lambda x,y: x+y,map(len, listOf15kElement),0)+ len(line))< 3999):
                listOf15kElement.append(line)

        else:
            if(text):
                listOf15k.append('\n'.join(listOf15kElement))
                listOf15kElement = [line]

    listOf15k.append('\n'.join(listOf15kElement))

    return [listOf15k, referenceList]


def translate(fileMD):
    translator = Translator(service_urls=urls)

    filename = os.fsdecode(fileMD)
    dir = ''
    filenameEn = translator.translate(filename, dest='en', src='de').text
    component = False

    try:
        f = open(directoryC + '/' + fileMD)
        dir += 'C/'
        component = True
    except:
        try:
            f = open(directoryN + '/' + fileMD)
            dir += 'N/'
        except:
            f = open(directoryT + '/' + fileMD)
            dir += 'T/'

    contentOfMdDE = f.read()
    listOf15k = check15k(contentOfMdDE, component)
    textEl = ''
    references = ''

    if(component):
        for rf in listOf15k[1]:
            references += translator.translate(rf, dest='en', src='de').text + '\n'

    for el in listOf15k[0]:
        textEl += translator.translate(el, dest='en', src='de').text + '\n'

    if(component):
        r = open(settings.CRAWLER_DIR + '/references/' + re.sub('/', '-', filenameEn.split('.md')[0]) + '.txt', 'w', encoding='utf-8')
        r.write(references)
        r.close()
    textEl = '[toc]\n \n' + textEl
    f = open(directoryEN + '/' + dir + re.sub('/', '-', filenameEn),'w', encoding='utf-8' )
    f.write(textEl)
    f.close()


if __name__ == "__main__":
    global directoryC
    global directoryN
    global directoryT
    global directoryEN

    filesForTranslation = []
    phase = str(sys.argv[1])

    if(str(phase) == '0'):
        directoryC = settings.BSI_DE + '/C'
        directoryN = settings.BSI_DE + '/N'
        directoryT = settings.BSI_DE + '/T'
        directoryEN = settings.BSI_EN

        files = os.listdir(directoryC)
        files.extend(os.listdir(directoryT))
        files.extend(os.listdir(directoryN))

    elif(str(phase) == '1'):
        directoryC = settings.TEMP_BSI_DE + '/C'
        directoryN = settings.TEMP_BSI_DE + '/N'
        directoryT = settings.TEMP_BSI_DE + '/T'
        directoryEN = settings.TEMP_BSI_EN

        modified, added, deleted = bsiImporter.checkFileAction()

        typesModified = modified('type')
        typesAdded = added.get('type')

        for el in typesModified:
            files = el['files']
            for file in files:
                filesForTranslation.append(file['filename'])

        for el in typesAdded:
            files = el['files']
            for file in files:
                filesForTranslation.append(file['filename'])


    else:
        raise ValueError('Please set a phase with phase 0|1')



    pool = Pool()
    pool.map(translate, files)