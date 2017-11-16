import json
from googletrans import Translator
import os

directoryContent = './content/'
directory = './content'
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
        'translate.google.at',
        'translate.google.pl',
        'translate.google.ad',
        'translate.google.ae',
        'translate.google.com.af',
        'translate.google.co.ao',
        'translate.google.com.ar',
        'translate.google.as',
        'translate.google.at',
        'translate.google.com.au',
        'translate.google.az',
        'translate.google.ba',
        'translate.google.com.bd',
        'translate.google.be',
        'translate.google.bf',
        'translate.google.bg',
        'translate.google.bh',
        'translate.google.bi',
        'translate.google.bj',
        'translate.google.com.bn',
        'translate.google.com.bo',
        'translate.google.com.br',
        'translate.google.bs',
        'translate.google.co.bw',
        'translate.google.by',
        'translate.google.com.bz',
        'translate.google.ca',
        'translate.google.cd',
        'translate.google.cf',
        'translate.google.cg',
        'translate.google.ch',
        'translate.google.ci',
        'translate.google.co.ck',
        'translate.google.cl',
        'translate.google.cm',
        'translate.google.cn',
        'translate.google.com.co',
        'translate.google.co.cr',
        'translate.google.com.cu',
        'translate.google.cv',
        'translate.google.com.cy',
        'translate.google.cz',
        'translate.google.dj',
        'translate.google.dk',
        'translate.google.dm',
        'translate.google.com.do',
        'translate.google.dz',
        'translate.google.com.ec',
        'translate.google.ee',
        'translate.google.com.eg',
        'translate.google.es',
        'translate.google.com.et',
        'translate.google.fi',
        'translate.google.com.fj',
        'translate.google.fm',
        'translate.google.fr',
        'translate.google.ga',
        'translate.google.ge',
        'translate.google.gg',
        'translate.google.com.gh',
        'translate.google.',
        'translate.google.com.gi',
        'translate.google.gm',
        'translate.google.gl',
        'translate.google.gp',
        'translate.google.gr',
        'translate.google.com.gt',
        'translate.google.gy',
        'translate.google.com.hk',
        'translate.google.hn',
        'translate.google.hr',
        'translate.google.ht',
        'translate.google.hu',
        'translate.google.id',
        'translate.google.ie',
        'translate.google.co.il',
        'translate.google.im',
        'translate.google.co.in',
        'translate.google.iq',
        'translate.google.is',
        'translate.google.it',
        'translate.google.je',
        'translate.google.com.jm',
        'translate.google.jo',
        'translate.google.co.jp',
        'translate.google.co.ke',
        'translate.google.com.kw',
        'translate.google.kz',
        'translate.google.la',
        'translate.google.con.lb',
        'translate.google.li',
        'translate.google.lk',
        'translate.google.co.ls',
        'translate.google.lt',
        'translate.google.lu',
        'translate.google.lv',
        'translate.google.com.ly',
        'translate.google.co.ma',
        'translate.google.md',
        'translate.google.me',
        'translate.google.mg',
        'translate.google.mk',
        'translate.google.ml',
        'translate.google.mn',
        'translate.google.ms',
        'translate.google.com.mt',
        'translate.google.mu',
        'translate.google.mv',
        'translate.google.mw',
        'translate.google.mx',
        'translate.google.com.my',
        'translate.google.co.mz',
        'translate.google.com.na',
        'translate.google.com.nf',
        'translate.google.com.ng',
        'translate.google.com.ni',
        'translate.google.ne',
        'translate.google.nl',
        'translate.google.no',
        'translate.google.com.np',
        'translate.google.nr',
        'translate.google.nu',
        'translate.google.co.nz',
        'translate.google.com.om',
        'translate.google.com.pa',
        'translate.google.com.pe',
        'translate.google.com.ph',
        'translate.google.com.pk',
        'translate.google.pn',
        'translate.google.pr',
        'translate.google.ps',
        'translate.google.pt',
        'translate.google.cpm.py',
        'translate.google.com.qa',
        'translate.google.ro',
        'translate.google.ru',
        'translate.google.rw',
        'translate.google.com.sa',
        'translate.google.com.sb',
        'translate.google.sc',
        'translate.google.se',
        'translate.google.com.sg',
        'translate.google.sh',
        'translate.google.si',
        'translate.google.sk',
        'translate.google.com.sl',
        'translate.google.sn',
        'translate.google.so',
        'translate.google.sm',
        'translate.google.st',
        'translate.google.com.sv',
        'translate.google.td',
        'translate.google.tg',
        'translate.google.co.th',
        'translate.google.com.tj',
        'translate.google.tk',
        'translate.google.tl',
        'translate.google.tm',
        'translate.google.tn',
        'translate.google.to',
        'translate.google.com.tr',
        'translate.google.tt',
        'translate.google.tw',
        'translate.google.co.tz',
        'translate.google.com.ua',
        'translate.google.co.ug',
        'translate.google.co.uk',
        'translate.google.com.uy',
        'translate.google.co.uz',
        'translate.google.com.vc',
        'translate.google.co.ve',
        'translate.google.vg',
        'translate.google.co.vi',
        'translate.google.com.vn',
        'translate.google.vu',
        'translate.google.ws',
        'translate.google.rs',
        'translate.google.co.za',
        'translate.google.co.zm',
        'translate.google.co.zw',
        'translate.google.cat',
        'translate.google.xxx',
    ])

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        first = " ".join(filename.split(" ", 1)[:1])
        if(first == 'B'):
            jsonFile = json.load(open(directoryContent + filename))
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
        else:
            return

if __name__ == '__main__':
    translate()