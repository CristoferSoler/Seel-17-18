import json
from googletrans import Translator
import os
import time
from multiprocessing import Pool

directoryContent = './test/'
directory = './test'
def generateText(object):
    text = []
    for ob in object:
        if(isinstance(ob,list)):
            liList = []
            for li in ob:
                liList.append(li.text)
            text.append(liList)
        else:
            text.append(ob.text)
    return text


def translate(file):
    translator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.co.kr',
        'translate.google.de',
        'translate.google.at',
        'translate.google.pl',
        'translate.google.ad',
    ])


    filename = os.fsdecode(file)
    first = " ".join(filename.split(" ", 1)[:1])
    if(first == 'B'):
        print(filename)
        jsonFile = json.load(open(directoryContent + filename))
        h1DE = jsonFile['h1']
        descriptionDE = jsonFile['description']['content']
        recomContentDE = jsonFile['recommendations']['content']
        subHeadersDEList = jsonFile['recommendations']['subheaders']
        subheaderDEList1 = []
        for subHeader in subHeadersDEList:
            subheaderDEList1.append((subHeader['h3'],subHeader['content']))


        h1EN = translator.translate(h1DE, dest='en', src='de').text

        descriptionENObject = translator.translate(descriptionDE, dest='en', src='de')
        descriptionEn = generateText(descriptionENObject)

        recomContentENObject = translator.translate(recomContentDE, dest='en', src='de')
        recomContentEN = generateText(recomContentENObject)

        subheaderEN = []
        for el in subheaderDEList1:
            translateObject = []
            translateObject.append(el[0])
            translateObject.append(el[1])
            translateObjectResponse = translator.translate(translateObject, dest='en', src='de')
            subheaderEN.append((translateObjectResponse[0].text,generateText(translateObjectResponse[1])))

        jsonFile['h1'] = h1EN
        jsonFile['description']['content'] = descriptionEn
        jsonFile['recommendations']['content'] = recomContentEN

        for i in range(0,len(jsonFile ['recommendations']['subheaders'])):
            jsonFile['recommendations']['subheaders'][i]['h3'] = subheaderEN[i][0]
            jsonFile['recommendations']['subheaders'][i]['content'] = subheaderEN[i][1]

        #print(jsonFile)
        #time.sleep(3)
    else:
        print("Kommt später")

if __name__ == '__main__':
    files = os.listdir(directory)
    start = time.time()
    for file in files:
        translate(file)
    print("Normal: ", time.time() - start)

    start = time.time()
    pool = Pool()
    pool.map(translate, files)
    print("MultiProcessing: ", time.time() - start)