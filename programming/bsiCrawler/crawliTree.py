import scrapy as sc
import json
from googletrans import Translator


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
        'translate.google.hu',
      ]

tree = {'Bausteine': {}, 'Elementare Gefährdungen': {}, 'Umsetzungshinweise': {}}
translator = Translator(service_urls=urls)

def generateParent(name):
    return {'text': name, 'nodes': []}

def generateChild(name):
    return {'text': name}

def generateTree(tree):
    bootstrapTree = []

    jsonTree = json.loads(tree)

    for key, value in jsonTree.items():
        dummy = generateParent(key)

        for key1, value1 in value.items():
            zweiterParent = generateParent(key1)

            for item in value1:
                zweiterParent['nodes'].append(generateChild(item))

            dummy['nodes'].append(zweiterParent)

        bootstrapTree.append(dummy)

    print(bootstrapTree)
    f = open('bsiTreeBootstrap' + '.txt', 'w')
    treeJson = json.dumps(bootstrapTree)
    f.write(treeJson)
    f.close()

#alle Links unter Bausteine, Gegenmaßnahmen und Maßnahmen holen
def get_links(response, h2Headline):
    links = []

    SET_SELCTOR = '#content'
    content = response.css(SET_SELCTOR)

    listOfH2sText = content.xpath('h2/text()')
    numberOfH2 = len(listOfH2sText)

    for i in range(0, numberOfH2):
        if (listOfH2sText[i].extract().strip() in h2Headline):
            lis = content.xpath('h2')[i].xpath('following-sibling::ul')[0].xpath('.').xpath('child::li')

            for li in lis:
                text = li.xpath('child::a').xpath('text()').extract()[0].strip()

                text = translator.translate(text, dest='en', src='de').text
                tree.get(h2Headline)[text] = []
                links.append("https://www.bsi.bund.de/" + li.xpath('child::a').xpath('@href').extract()[0])
            return links


class bsiSpider(sc.Spider):
    name = "bsiSpider"
    start_urls = ['https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/itgrundschutzKompendium_node.html']

    def parse(self, response):
        urlsB = get_links(response, 'Bausteine')
        urlsG = get_links(response, 'Elementare Gefährdungen')
        urlsM = get_links(response, 'Umsetzungshinweise')

        for b in urlsB:
            yield sc.Request(b, callback=self.parseLinkList, dont_filter=True)

        for g in urlsG:
            yield sc.Request(g, callback=self.parseLinkListG, dont_filter=True)

        for m in urlsM:
            yield sc.Request(m, callback=self.parseLinkListM, dont_filter=True)


    #folgende 3 Funktionen extrahieren die Links aus den Unterseiten
    def parseLinkList(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1').xpath('text()').extract()[0].strip()
        h1En = translator.translate(h1, dest='en', src='de').text

        for link in response.css('.RichTextIntLink.Basepage'):
            text = link.xpath('text()').extract()[0].strip()

            text = translator.translate(text, dest='en', src='de').text

            tree['Bausteine'][h1En].append(text)

    def parseLinkListG(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1').xpath('text()').extract()[0].strip()
        h1En = translator.translate(h1, dest='en', src='de').text

        for link in response.css('.RichTextIntLink.Basepage'):
            text = link.xpath('text()').extract()[0].strip()
            text = translator.translate(text, dest='en', src='de').text

            tree['Elementare Gefährdunge'][h1En].append(text)


    def parseLinkListM(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1').xpath('text()').extract()[0].strip()

        h1En = translator.translate(h1, dest='en', src='de').text


        for link in response.css('.RichTextIntLink.Basepage'):
            text = link.xpath('text()').extract()[0].strip()

            text = translator.translate(text, dest='en', src='de').text
            tree['Umsetzungshinweise'][h1En].append(text)

    #Fertig mit dem Auslesen der Struktur
    def closed(self, reason):
        # manuelle Übersetzung, weil google anders übersetzt
        tree['Components'] = tree.pop('Bausteine')
        tree['Elementary hazards'] = tree.pop('Elementare Gefährdungen')
        tree['implementation notes'] = tree.pop('Umsetzungshinweise')
        generateTree(json.dumps(tree))