import json
from googletrans import Translator

directory = '/Users/Jonathan/PycharmProjects/Seel-17-18/programming/bsiCrawler/content/'

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
        'translate.google.com',
        'translate.google.co.kr',
        'translate.google.de',
    ])
    descriptionEn = []

    jsonFile = json.load(open(directory + 'B 1.1 Organisation.json'))
    print(jsonFile)
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
        jsonFile['recommendations']['subheaders'][i]['h1'] = subheaderEN[i][0]
        jsonFile['recommendations']['subheaders'][i]['content'] = subheaderEN[i][1]

    print(jsonFile)


if __name__ == '__main__':
    translate()