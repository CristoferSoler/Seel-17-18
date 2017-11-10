import scrapy as sc
import requests as req
import os

#Yandex Parameter
APIKey = 'trnsl.1.1.20171104T205815Z.06e73f15109112a3.dabfe16a4052f8e8beb0d0263b8f6db5d71130b3'
lang = 'de-en'
textFormat = 'plain'

#Other Costant
dicOfContent = os.getcwd() + '/content/'


def sendRequestToYandex(header,text):
    if(len(text)< 10000):
        r = req.post("https://translate.yandex.net/api/v1.5/tr.json/translate?key=" + APIKey +
                          "&text=" + text + "&lang=" + lang + "&format=" + textFormat).json()
        yandexResponseText = r["text"][0]
        writeFile(header, yandexResponseText)

    else:
        print("Tooo long")


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

def writeFile(title,content):

    f = open(dicOfContent + title +'.txt', 'w')
    f.write(title+'\n')
    f.write(content)
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


    def parseLinkList(self, response):
        siteUrl = []
        SET_SELECTOR = '.RichTextIntLink.Basepage'
        for link in response.css(SET_SELECTOR):
            siteUrl.append("https://www.bsi.bund.de/" + link.xpath('@href').extract()[0])
        #print(len(siteUrl))
        #print('-----------')

        for link in siteUrl:
            yield sc.Request(link, callback=self.parse_following_urls, dont_filter=True)

    def parse_following_urls(self, response):

        headline = ''
        beschreibung = ''
        beschreibung_content = ''
        massnahme = ''
        massnahmeContent = ''

        SET_SELCTOR = '#content'

        content = response.css(SET_SELCTOR)
        headline = content.xpath('h1/text()').extract()[0].strip()
        print(headline)

        headers = content.xpath('h2')
        if len(headers) != 0:
            beschreibung = headers[0].xpath('./text()').extract()[0]

            for ps in headers[0].xpath('following-sibling::p'):
                if(ps.extract() == headers[1].xpath('following-sibling::p')[0].extract()):
                   break
                else:
                    #Beschreibungstext
                    beschreibung_content = beschreibung_content + ps.xpath('./text()').extract()[0].strip()
            #print(beschreibung)
            sendRequestToYandex(headline,beschreibung_content)
            #print(massnahme)
            #print(massnahmeContent)
        else:
            print(beschreibung)
            beschreibung_content= beschreibung_content + content.xpath('h1')[0].xpath('following::p/text()').extract()[0].strip()
            print(beschreibung_content)

        headerh3 = content.xpath('h3/text()')
        headerh3xpath = content.xpath('h3')
        numberofh3 = len(headerh3)

        allP = headers[2].xpath('following-sibling::p')

        #for i in range(1,len(allP)):

            #print(ps.extract())
            #for i in range(0, numberofh3):
             #   #print('test')
                #print(headerh3[i])
              #  if (headerh3[i].extract().strip() in 'Planung und Konzeption'):
               #     #print('test1')
                #    if (ps.extract() == headerh3xpath[i].xpath('following-sibling::p')[0].extract()):
                 #       break
                  #  else:
                   #     print(ps.xpath('text()').extract()[0])
                    #    break
                        # Beschreibungstext
                        #massnahmeContent = massnahmeContent + ps.xpath('/text()').extract()[0].strip()

        #print(massnahme)
        #print(massnahmeContent)

        print("-----------------------------------------")

