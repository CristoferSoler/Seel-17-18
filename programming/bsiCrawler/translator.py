import json
from googletrans import Translator
import os
import codecs
import re
import time

directoryContent = './content/'
directory = './content'
directoryContentEN = './contentEn/'

def check15k(list):
    size = 0
    for li in list:
        size += len(li)


    if size < 14999:
        return True
    else:
        print('Zuviel')
        False

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


def translate():
    translator = Translator(service_urls=[
        'translate.google.by',

    ])

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.json'):
            first = " ".join(filename.split(" ", 1)[:1])
            if(first == 'B'):
                continue
                print(filename)
                test = directoryContent + file


                jsonFile = json.load(open(test))
                h1DE = jsonFile['h1']
                descriptionDE = jsonFile['description']['content']
                recomContentDE = jsonFile['recommendations']['content']
                subHeadersDEList = jsonFile['recommendations']['subheaders']
                subheaderDEList1 = []
                for subHeader in subHeadersDEList:
                    subheaderDEList1.append((subHeader['h3'],subHeader['content']))


                h1EN = translator.translate(h1DE, dest='en', src='de').text
                if (check15k(descriptionDE)):
                    #print(descriptionDE)
                    descriptionENObject = translator.translate(descriptionDE, dest='en', src='de')
                    descriptionEn = generateText(descriptionENObject)
                else:
                    descriptionEn = descriptionDE

                if (check15k(recomContentDE)):
                    recomContentENObject = translator.translate(recomContentDE, dest='en', src='de')
                    recomContentEN = generateText(recomContentENObject)
                else:
                    recomContentEN = recomContentDE

                subheaderEN = []
                for el in subheaderDEList1:
                    translateObject = []
                    translateObject.append(el[0])
                    translateObject.append(el[1])
                    if (check15k(translateObject)):
                        translateObjectResponse = translator.translate(translateObject, dest='en', src='de')
                        #print(translateObject)
                        subheaderEN.append((translateObjectResponse[0].text,generateText(translateObjectResponse[1])))
                    else:
                        subheaderEN.append((el[0],el[1]))

                jsonFile['h1'] = h1EN
                jsonFile['description']['content'] = descriptionEn
                jsonFile['recommendations']['content'] = recomContentEN

                for i in range(0,len(jsonFile ['recommendations']['subheaders'])):
                    jsonFile['recommendations']['subheaders'][i]['h1'] = subheaderEN[i][0]
                    jsonFile['recommendations']['subheaders'][i]['content'] = subheaderEN[i][1]

                f = open(directoryContentEN + re.sub('/', '-', h1EN) + '.json', 'w')
                f.write(json.dumps(jsonFile))
                f.close()
                time.sleep(3)

            else:
                print(file)
                test = directoryContent + file
                jsonFile = json.load(open(test))
                h1DE = jsonFile['h1']
                descriptionDE = jsonFile['content']


                h1EN = translator.translate(h1DE, dest='en', src='de').text
                if (check15k(descriptionDE)):
                    descriptionENObject = translator.translate(descriptionDE, dest='en', src='de')
                    descriptionEn = generateText(descriptionENObject)
                else:
                    descriptionEn = descriptionDE

                try:
                    subHeaderDE = jsonFile['subheaders']
                    if (check15k(subHeaderDE)):
                        subHeaderENObject = translator.translate(subHeaderDE, dest='en', src='de')
                        subHeaderEN = generateText(subHeaderENObject)
                    else:
                        subHeaderEN = subHeaderDE

                    jsonFile['subheaders'] = subHeaderEN

                except:
                     pass

                jsonFile['h1'] = h1EN
                jsonFile['content'] = descriptionEn
                jsonFile['subheaders'] = subHeaderEN

                f = open(directoryContentEN + re.sub('/', '-', h1EN) + '.json', 'w')
                f.write(json.dumps(jsonFile))
                f.close()


if __name__ == '__main__':
    translate()