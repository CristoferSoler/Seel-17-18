import scrapy as sc
import os
import re
import functools
from markdownify import markdownify as md

#TODO
#- einzelene Unterkapitel auslesen

#Yandex Parameter
APIKey = 'trnsl.1.1.20171104T205815Z.06e73f15109112a3.dabfe16a4052f8e8beb0d0263b8f6db5d71130b3'
lang = 'de-en'
textFormat = 'plain'

#Other Costant
dicOfContent = os.getcwd() + '/content/'

directoryContent = './md/'
directoryContentComponent = '/B/'
directoryContentNotes = '/H/'
directoryContentThreats = '/T/'

def sendRequestToYandex(text):
    '''if(len(text)< 10000):
        r = req.post("https://translate.yandex.net/api/v1.5/tr.json/translate?key=" + APIKey +
                          "&text=" + text + "&lang=" + lang + "&format=" + textFormat).json()
        yandexResponseText = r["text"][0]
        #writeFile(header, yandexResponseText)

    else:
        print("Tooo long")'''
    return text


# alle Links die unter einer h2 Headline aufgelistet sind
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
                links.append("https://www.bsi.bund.de/" + li.xpath('child::a').xpath('@href').extract()[0])
            return links

def writeComponentJSON(h1, description_h2, description_content, recom_header, recom_content, recom,wholeText):
    f = open(dicOfContent + re.sub('/','-',h1) + '.json', 'w')
    jsonPart1 = '{"h1":"' + h1 + '", "description": { "h2":"' +  description_h2 +'", "content":['

    for i in range(0,len(description_content)):
        if (isinstance(description_content[i], list)):
            jsonPart1 += '['
            for j in range(0, len(description_content[i])):
                if (j == len(description_content[i]) - 1):
                    jsonPart1 += '"' + description_content[i][j] + '"]'
                else:
                    jsonPart1 += '"' + description_content[i][j] + '",'

            if (i == len(description_content) - 1):
                break
            else:
                    jsonPart1 += ','
        else:
            if (i == len(description_content) - 1):
                jsonPart1 += '"' + description_content[i] + '"'
            else:
                jsonPart1 += '"' + description_content[i] + '",'

    jsonPart1 += ']' + '},"recommendations":{"h2":"' +  recom_header + '","content":['

    for i in range(0,len(recom_content)):
        if (isinstance(recom_content[i], list)):
            jsonPart1 += '['
            for j in range(0, len(recom_content[i])):
                if (j == len(recom_content[i]) - 1):
                    jsonPart1 += '"' + recom_content[i][j] + '"]'
                else:
                    jsonPart1 += '"' + recom_content[i][j] + '",'

            if (i == len(recom_content) - 1):
                break
            else:
                    jsonPart1 += ','
        else:
            if (i == len(recom_content) - 1):
                jsonPart1 += '"' + recom_content[i] + '"'
            else:
                jsonPart1 += '"' + recom_content[i] + '",'

    jsonPart1 +=  '],"subheaders":['
    for i in range(0, len(recom)):
        subHeaderObject = '{"h3":"' + recom[i][0] + '", "content":['




        for j in range(0, len(recom[i][1])):
            if (isinstance(recom[i][1][j], list)):
                subHeaderObject += '['
                for k in range(0, len(recom[i][1][j])):
                    if (k == len(recom[i][1][j]) - 1):
                        subHeaderObject += '"' + recom[i][1][j][k] + '"]'
                    else:
                        subHeaderObject += '"' + recom[i][1][j][k] + '",'

                if (j == len(recom[i][1]) - 1):
                    break
                else:
                    subHeaderObject += ','
            else:
                if (j == len(recom[i][1]) - 1):
                    subHeaderObject += '"' + recom[i][1][j] + '"'
                else:
                    subHeaderObject += '"' + recom[i][1][j] + '",'

        subHeaderObject += ']}'
        jsonPart1  = jsonPart1 + subHeaderObject
        if(i == len(recom)-1):
            break
        else:
            jsonPart1 = jsonPart1 + ','

    jsonPart1 = jsonPart1 + ']}, "wholeText": "' + wholeText + '"}'

    f.write(jsonPart1)
    f.close()

def writeThreadJSON(h1,content,listOfExpample):
    f = open(dicOfContent + re.sub('/', '-', h1) + '.json', 'w')
    jsonPart1 = '{"h1":"' + h1 + '","content":['\

    for i in range(0,len(content)):
        if (isinstance(content[i], list)):
            jsonPart1 += '['
            for j in range(0, len(content[i])):
                if (j == len(content[i]) - 1):
                    jsonPart1 += '"' + content[i][j] + '"]'
                else:
                    jsonPart1 += '"' + content[i][j] + '",'

            if (i == len(content) - 1):
                break
            else:
                    jsonPart1 += ','
        else:
            if (i == len(content) - 1):
                jsonPart1 += '"' + content[i] + '"'
            else:
                jsonPart1 += '"' + content[i] + '",'
    jsonPart1 +=']'
    if(len(listOfExpample) != 0):
        jsonPart1 += ',"subheaders":['

    for i in range(0, len(listOfExpample)):
        if (i == len(listOfExpample) - 1):
            jsonPart1 += '"' + listOfExpample[i] + '"]'
        else:
            jsonPart1 += '"' + listOfExpample[i] + '",'

    jsonPart1 += '}'

    f.write(jsonPart1)
    f.close()


def allUnderH2(list):
    returnList = []
    for el in list:
        if "h2" not in el.extract():
            returnList.append(el)
        else:
            return returnList

    return returnList


def getContentOfH2(h2):

    return 'test'

    '''
    for element in allElementsUnderH2:
        if ("h2" not in element.extract()):

        else:
            break
'''


class bsiSpider(sc.Spider):
    name = "bsiSpider"
    #startpage to crawl
    start_urls = ['https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/itgrundschutzKompendium_node.html']

    def parse(self, response):
        print('Start Crawling the content of the BSI')
        #get all links under Bausteine, Elementare Gefährdungen und Umsetzungshinweise
        urlsG = get_links(response,'Elementare Gefährdungen')
        urlsB = get_links(response,'Bausteine')
        urlsU = get_links(response,'Umsetzungshinweise')

        #go to every link
        for g in urlsG:
           yield sc.Request(g, callback=self.parseLinkList_G, dont_filter=True)

        for b in urlsB:
           yield sc.Request(b, callback=self.parseLinkList, dont_filter=True)

        for u in urlsU:
           yield sc.Request(u, callback=self.parseLinkList_H, dont_filter=True)

    def parseLinkList(self, response):
        siteUrl = []
        SET_SELECTOR = '.RichTextIntLink.Basepage'
        for link in response.css(SET_SELECTOR):
            siteUrl.append("https://www.bsi.bund.de/" + link.xpath('@href').extract()[0])

        for link in siteUrl:
            yield sc.Request(link, callback=self.parse_following_urls, dont_filter=True)

    def parseLinkList_H(self, response):
        siteUrl = []
        SET_SELECTOR = '.RichTextIntLink.Basepage'
        for link in response.css(SET_SELECTOR):
            siteUrl.append("https://www.bsi.bund.de/" + link.xpath('@href').extract()[0])

        for link in siteUrl:
            yield sc.Request(link, callback=self.parse_following_urls_H, dont_filter=True)

    def parseLinkList_G(self, response):
        siteUrl = []
        SET_SELECTOR = '.RichTextIntLink.Basepage'
        for link in response.css(SET_SELECTOR):
            siteUrl.append("https://www.bsi.bund.de/" + link.xpath('@href').extract()[0])

        for link in siteUrl:
            yield sc.Request(link, callback=self.parse_following_urls_of_G, dont_filter=True)

    def parse_following_urls_of_G(self,response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1/text()').extract()[0].strip()

        h1Element = content.xpath('h1')
        h2Element = content.xpath('h2')
        # h2Element = h2Element.pop(0)

        allRelatedContentHTML = h1Element[0].xpath(
            '.|following-sibling::h3|following-sibling::h4|following-sibling::p[not(@class)]|following-sibling::ul|following-sibling::h2|following-sibling::h1|following-sibling::li').extract()
        allRelatedContentOneStringHTML = functools.reduce(lambda x, y: x + y, allRelatedContentHTML)

        f = open(directoryContent + '/' + directoryContentThreats + re.sub('/', '-', h1) + '.md', 'w')
        f.write(md(allRelatedContentOneStringHTML))
        f.close()
        '''SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)

        h1 = content.xpath('h1/text()').extract()[0].strip().replace("\"","").replace("\n","")

        h3 = content.xpath('h3')

        contentOfPage = content.xpath('h1').xpath('following-sibling::p|following-sibling::ul|following-sibling::h3|following-sibling::h2')

        if not contentOfPage:
            return

        contents = []

        for content in contentOfPage:
            if ('h2' in content.extract()):
                break

            if('h3' not in content.extract()):
                if(len(content.xpath('child::li'))!=0):
                    ul = []
                    for li in content.xpath('child::li'):
                        ul.append(li.select('string()').extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
                    contents.append(ul)
                else:
                    contents.append(content.select('string()').extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
            else:
                break

        listOfExample = []
        if(len(h3.xpath('following-sibling::ul')) != 0):
            ul = h3.xpath('following-sibling::ul')[0]
            listOfExample = []
            for li in ul.xpath('child::li'):
                listOfExample.append(li.select('string()').extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))

        writeThreadJSON(h1,contents,listOfExample)
        '''

    def parse_following_urls_H(self, response):

        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1/text()').extract()[0].strip()

        h1Element = content.xpath('h1')
        h2Element = content.xpath('h2')
        #h2Element = h2Element.pop(0)

        allRelatedContentHTML = h2Element[1].xpath('.|following-sibling::h3|following-sibling::h4|following-sibling::p[not(@class)]|following-sibling::ul|following-sibling::h2|following-sibling::h1|following-sibling::li').extract()
        allRelatedContentOneStringHTML = functools.reduce(lambda x,y: x+y,allRelatedContentHTML)

        f = open(directoryContent + '/' + directoryContentNotes + re.sub('/', '-', h1) + '.md', 'w')
        f.write(md(allRelatedContentOneStringHTML))
        f.close()

    def parse_following_urls(self, response):

        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1/text()').extract()[0].strip()

        h1Element = content.xpath('h1')
        h2Element = content.xpath('h2')
        #h2Element = h2Element.pop(0)

        allRelatedContentHTML = h2Element[1].xpath('.|following-sibling::h3|following-sibling::h4|following-sibling::p[not(@class)]|following-sibling::ul|following-sibling::h2|following-sibling::h1|following-sibling::li').extract()
        allRelatedContentOneStringHTML = functools.reduce(lambda x,y: x+y,allRelatedContentHTML)

        f = open(directoryContent + '/' + directoryContentComponent + re.sub('/', '-', h1) + '.md', 'w')
        f.write(md(allRelatedContentOneStringHTML))
        f.close()

        #
        # headers = content.xpath('h2').extract()


        '''print(headers)
        #delete the first h2 headline because it is the Schnellübersicht
        headers1 = headers.pop(0)
        description_content = []
        recom_content = []
        recom = []

        page = {'title': h1,'h2':[]}

        #description_h2 = headers[0].xpath('./text()').extract()[0]
        if (len(headers1) != 0):
            for h2 in headers1:

                h2Element = {'h2Title': h2.xpath('./text()').extract()[0],'content':[],'h3':[],}

                h2elementsHeadlines = h2.xpath(getAllh2h3)
                for el in h2elementsHeadlines:
                    #alle h3 Headlines
                    if "h2" not in el.extract():
                        #check ob h3 element kommt oder conent unter h2
                        if "h3" in el.extract():
                            h3Element = {'title': h3El.xpath('./text()').extract()[0], 'content': [], 'h4': []}
                            for h3El in el.xpath('following-sibling::h3|following-sibling::h4|following-sibling::p|following-sibling::ul'):
                                #check ob h3 oder inhalt unter h3 kommt
                                if "h3" not in h3El.extract():
                                    #schauen ob h4 headline kommt oder h3 inhalt
                                    if "h4" not in h3El.extract():
                                        #h3 zusammenbauen
                                        if (len(h3El.xpath('child::li')) != 0):
                                            ul = []
                                            for li in h3El.xpath('child::li'):
                                                ul.append(li.select("string()").extract()[0].strip().replace("\"", "").replace("\n", "").replace("\\", "/"))
                                            h3Element['content'].append(ul)

                                        else:
                                            h3Element['content'].append(h3El.select("string()").extract()[0].strip().replace("\"", "").replace("\n", "").replace("\\", "/"))
                                    else:
                                        # h4 zusammenbauen
                                        continue

                                else:
                                    #zum nächsten h3 gehen und h3 zu h2 adden
                                    continue

                        else:
                            #content unter h2 Headline hinzufügen
                           h2Element['content'].append(el.select("string()").extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
                    else:
                        #zum nächsten h2 gehen
                        page['h2'].append(h2Element)
                        continue

            
            #Beschreibung
            for ps in headers[0].xpath(
                    'following-sibling::p|following-sibling::ul|following-sibling::h2|following-sibling::h3'):
                if ("h2" not in ps.extract()):
                    if (len(ps.xpath('child::li')) != 0):
                        ul = []
                        for li in ps.xpath('child::li'):
                            ul.append(li.select("string()").extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
                        description_content.append(ul)

                    else:
                        description_content.append(ps.select("string()").extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
                else:
                    break

            h3Headers = headers[2].xpath('following-sibling::h3')
            recom_header = headers[2].xpath('./text()').extract()[0]
            for ps in headers[2].xpath(
                    'following-sibling::p|following-sibling::ul|following-sibling::h2|following-sibling::h3'):
                if ("h3" not in ps.extract()):
                    if (len(ps.xpath('child::li')) != 0):
                        ul = []
                        for li in ps.xpath('child::li'):
                            ul.append(li.select("string()").extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
                        recom_content.append(ul)

                    else:
                        recom_content.append(ps.select("string()").extract()[0].strip().replace("\"","").replace("\n","").replace("\\","/"))
                else:
                    break

            for h3 in h3Headers:
                h3_head = h3.select("string()").extract()[0].strip()

                h3_content = []
                for ps in h3.xpath(
                        'following-sibling::p|following-sibling::ul|following-sibling::h3'):
                    if ("h3" not in ps.extract()):
                        if (len(ps.xpath('child::li')) != 0):
                            ul = []
                            for li in ps.xpath('child::li'):
                                ul.append(
                                    li.select("string()").extract()[0].strip().replace("\"", "").replace("\n", "").replace("\\","/"))
                            h3_content.append(ul)

                        else:
                            h3_content.append(ps.select("string()").extract()[0].strip().replace("\"", "").replace("\n", "").replace("\\","/"))
                    else:
                        break

                if (len(h3_content) != 0):
                    recom_tupel = (h3_head, h3_content)
                    recom.append(recom_tupel)
                else:
                    break


            wholeText = ''
            
            h1 = sendRequestToYandex(h1).replace("\"","")
            description_h2 = sendRequestToYandex(description_h2).replace("\"","")
            description_content = sendRequestToYandex(description_content).replace("\"","").replace("\n","")

            recom_header = sendRequestToYandex(recom_header).replace("\"","")
            recom_content = sendRequestToYandex(recom_content).replace("\"","").replace("\n","")

            wholeText = h1 + " " + description_content + " " + recom_content

            for i in range(0, len(recom)):
                recom[i] = (sendRequestToYandex(recom[i][0]).replace("\"","").replace("\n",""), sendRequestToYandex(recom[i][1]).replace("\"","").replace("\n",""))
                wholeText = wholeText + recom[i][1]
            
            writeComponentJSON(h1.replace("\"","").replace("\\","/"), description_h2.replace("\"","").replace("\\","/"), description_content, recom_header.replace("\"","").replace("\\","/"), recom_content, recom,wholeText)
            '''

    def closed(self, reason):
        print('Crawler is finshed')
        print('Start the translation of the bsi content to english')
        #übersetzung einbaune
