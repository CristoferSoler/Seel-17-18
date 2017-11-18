import scrapy as sc
import requests as req
import os
import re
import json

#Yandex Parameter
APIKey = 'trnsl.1.1.20171104T205815Z.06e73f15109112a3.dabfe16a4052f8e8beb0d0263b8f6db5d71130b3'
lang = 'de-en'
textFormat = 'plain'

#Other Costant
dicOfContent = os.getcwd() + '/content/'



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

class bsiSpider(sc.Spider):
    name = "bsiSpider"
    start_urls = ['https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/itgrundschutzkataloge_node.html']

    def parse(self, response):
        urlsB = get_links(response,'Bausteine')
        urlsG = get_links(response,'Gefährdungskataloge')
        urlsM = get_links(response,'Maßnahmenkataloge')

        #for b in urlsB:
        #   yield sc.Request(b, callback=self.parseLinkList, dont_filter=True)

        for g in urlsG:
            yield sc.Request(g, callback=self.parseLinkListG, dont_filter=True)

        for m in urlsM:
            yield sc.Request(m, callback=self.parseLinkListG, dont_filter=True)

    def parseLinkList(self, response):
        siteUrl = []
        SET_SELECTOR = '.RichTextIntLink.Basepage'
        for link in response.css(SET_SELECTOR):
            siteUrl.append("https://www.bsi.bund.de/" + link.xpath('@href').extract()[0])

        for link in siteUrl:
            yield sc.Request(link, callback=self.parse_following_urls, dont_filter=True)

    def parseLinkListG(self, response):
        siteUrl = []
        SET_SELECTOR = '.RichTextIntLink.Basepage'
        for link in response.css(SET_SELECTOR):
            siteUrl.append("https://www.bsi.bund.de/" + link.xpath('@href').extract()[0])

        for link in siteUrl:
            yield sc.Request(link, callback=self.parse_following_urls_of_G, dont_filter=True)

    def parse_following_urls_of_G(self,response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)

        h1 = content.xpath('h1/text()').extract()[0].strip().replace("\"","").replace("\n","")

        h3 = content.xpath('h3')

        contentOfPage = content.xpath('h1').xpath('following-sibling::p|following-sibling::ul|following-sibling::h3|following-sibling::h2')

        contents = []

        for content in contentOfPage:
            if ('h2' in content.extract()):
                break

            if('h3' not in content.extract()):
                if(len(content.xpath('child::li'))!=0):
                    ul = []
                    for li in content.xpath('child::li'):
                        ul.append(li.select('string()').extract()[0].strip().replace("\"","").replace("\n",""))
                    contents.append(ul)
                else:
                    contents.append(content.select('string()').extract()[0].strip().replace("\"","").replace("\n",""))
            else:
                break

        listOfExample = []
        if(len(h3.xpath('following-sibling::ul')) != 0):
            ul = h3.xpath('following-sibling::ul')[0]
            listOfExample = []
            for li in ul.xpath('child::li'):
                listOfExample.append(li.select('string()').extract()[0].strip().replace("\"","").replace("\n",""))

        writeThreadJSON(h1,contents,listOfExample)

    def parse_following_urls(self, response):

        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)

        h1 = content.xpath('h1/text()').extract()[0].strip()

        headers = content.xpath('h2')

        description_content = []
        recom_content = []
        recom = []

        if (len(headers) != 0):
            description_h2 = headers[0].xpath('./text()').extract()[0]

            #Beschreibung
            for ps in headers[0].xpath(
                    'following-sibling::p|following-sibling::ul|following-sibling::h2|following-sibling::h3'):
                if ("h2" not in ps.extract()):
                    if (len(ps.xpath('child::li')) != 0):
                        ul = []
                        for li in ps.xpath('child::li'):
                            ul.append(li.select("string()").extract()[0].strip().replace("\"","").replace("\n",""))
                        description_content.append(ul)

                    else:
                        description_content.append(ps.select("string()").extract()[0].strip().replace("\"","").replace("\n",""))
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
                            ul.append(li.select("string()").extract()[0].strip().replace("\"","").replace("\n",""))
                        recom_content.append(ul)

                    else:
                        recom_content.append(ps.select("string()").extract()[0].strip().replace("\"","").replace("\n",""))
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
                                    li.select("string()").extract()[0].strip().replace("\"", "").replace("\n", ""))
                            h3_content.append(ul)

                        else:
                            h3_content.append(ps.select("string()").extract()[0].strip().replace("\"", "").replace("\n", ""))
                    else:
                        break

                if (len(h3_content) != 0):
                    recom_tupel = (h3_head, h3_content)
                    recom.append(recom_tupel)
                else:
                    break


            wholeText = ''
            '''
            h1 = sendRequestToYandex(h1).replace("\"","")
            description_h2 = sendRequestToYandex(description_h2).replace("\"","")
            description_content = sendRequestToYandex(description_content).replace("\"","").replace("\n","")

            recom_header = sendRequestToYandex(recom_header).replace("\"","")
            recom_content = sendRequestToYandex(recom_content).replace("\"","").replace("\n","")

            wholeText = h1 + " " + description_content + " " + recom_content

            for i in range(0, len(recom)):
                recom[i] = (sendRequestToYandex(recom[i][0]).replace("\"","").replace("\n",""), sendRequestToYandex(recom[i][1]).replace("\"","").replace("\n",""))
                wholeText = wholeText + recom[i][1]
            '''
            writeComponentJSON(h1.replace("\"",""), description_h2.replace("\"",""), description_content, recom_header.replace("\"",""), recom_content, recom,wholeText)


