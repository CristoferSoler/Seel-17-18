import scrapy as sc
import json

tree = {'Bausteine': {}, 'Gefährdungskataloge': {}, 'Maßnahmenkataloge': {}}


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
                tree.get(h2Headline)[text] = []

                links.append("https://www.bsi.bund.de/" + li.xpath('child::a').xpath('@href').extract()[0])
            return links


class bsiSpider(sc.Spider):
    name = "bsiSpider"
    start_urls = ['https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/itgrundschutzkataloge_node.html']

    def parse(self, response):
        urlsB = get_links(response, 'Bausteine')
        urlsG = get_links(response, 'Gefährdungskataloge')
        urlsM = get_links(response, 'Maßnahmenkataloge')

        for b in urlsB:
            yield sc.Request(b, callback=self.parseLinkList, dont_filter=True)

        for g in urlsG:
            yield sc.Request(g, callback=self.parseLinkListG, dont_filter=True)

        for m in urlsM:
            yield sc.Request(m, callback=self.parseLinkListM, dont_filter=True)


    def parseLinkList(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1').xpath('text()').extract()[0].strip()

        #Deutsche Dummköpfe
        h1 = "".join(h1.split(" ", 1))

        for link in response.css('.RichTextIntLink.Basepage'):
            text = link.xpath('text()').extract()[0].strip()
            tree['Bausteine'][h1].append(text)

    def parseLinkListG(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1').xpath('text()').extract()[0].strip()

        #Deutsche Dummköpfe
        h1 = "".join(h1.split(" ", 1))

        for link in response.css('.RichTextIntLink.Basepage'):
            text = link.xpath('text()').extract()[0].strip()
            tree['Gefährdungskataloge'][h1].append(text)

    def parseLinkListM(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1').xpath('text()').extract()[0].strip()

        #Deutsche Dummköpfe
        if('M 4 Hard- und Software' == h1):
            h1 = 'M 4 Hardware und Software'

        #Deutsche Dummköpfe
        h1 = "".join(h1.split(" ", 1))

        for link in response.css('.RichTextIntLink.Basepage'):
            text = link.xpath('text()').extract()[0].strip()
            tree['Maßnahmenkataloge'][h1].append(text)

    #Fertig mit dem Auslesen der Struktur
    def closed(self, reason):
        generateTree(json.dumps(tree))