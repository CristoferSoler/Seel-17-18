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
            jsonPart1 += '"ul":['
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
            jsonPart1 += '"ul":['
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
                subHeaderObject += '"ul":['
                for k in range(0, len(recom[i][1][j])):
                    if (j == len(recom[i][1][j]) - 1):
                        subHeaderObject += '"' + recom[i][1][j][k] + '"]'
                    else:
                        subHeaderObject += '"' + recom[i][1][j][k] + '",'

                if (i == len(recom[i][1][j]) - 1):
                    break
                else:
                    subHeaderObject += ','
            else:
                if (i == len(recom[i][1]) - 1):
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

def writeThreadJSON(h1,content):
    f = open(dicOfContent + re.sub('/', '-', h1) + '.json', 'w')
    content =re.sub('\n',' ' , content)
    jsonPart1 = '{"h1":"' + h1 + '","content":"'+ content + '"}'
    f.write(jsonPart1)
    f.close()

class bsiSpider(sc.Spider):
    name = "bsiSpider"
    start_urls = ['https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/itgrundschutzkataloge_node.html']

    def parse(self, response):
        urlsB = get_links(response,'Bausteine')
        urlsG = get_links(response,'Gefährdungskataloge')
        urlsM = get_links(response,'Maßnahmenkataloge')

        for b in urlsB:
            yield sc.Request(b, callback=self.parseLinkList, dont_filter=True)

        #for g in urlsG:
        #    yield sc.Request(g, callback=self.parseLinkListG, dont_filter=True)

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

        h1 = content.xpath('h1/text()').extract()[0].strip()

        h3 = content.xpath('h3')

        contentOfPage = content.xpath('h1').xpath('following-sibling::p|following-sibling::ul')

        contents = ''

        for content in contentOfPage:
            if('h3' not in content.extract()):
                if(len(content.xpath('child::li'))!=0):
                    for li in content.xpath('child::li'):
                        print('Liste')
                        contents = contents + "- " + li.select('string()').extract()[0].strip()
                else:
                    contents = contents + content.select('string()').extract()[0].strip()
            else:
                break

        writeThreadJSON(h1,contents)

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


