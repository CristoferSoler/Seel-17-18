import functools
import re
from os import environ

import scrapy as sc
import django
import sys
from markdownify import markdownify as md

'''
This module collects roughly the data from the BSI.
For this purpose, the crawler receives a start address and goes through all links from this address under 
Elementary Hazards, Building Blocks, and Implementation Notes and from there all links. And so you get the content
 of the BSI. Next, the content is converted from html to md and stored in a folder structure.  
'''

sys.path.append(r'..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings

# directorys for the german content of the bsi
#directoryContent = './md/'
directoryContentComponent = '/C/'
directoryContentNotes = '/N/'
directoryContentThreats = '/T/'
xpathString = '.|following-sibling::h3|following-sibling::h4|following-sibling::p[not(@class)]|following-sibling::ul|following-sibling::h2|following-sibling::h1|following-sibling::li'


# get all links under a h2Headline what can be Elemetare Gefährdungen, Bausteine and Umsetzungshinweise
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


class bsiSpider(sc.Spider):
    name = "bsiSpider"
    # startpage to crawl
    start_urls = [
        'https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/itgrundschutzKompendium_node.html']

    #update = 0|1: 0 means first setup 1 means update the bsi
    def __init__(self,phase='',*args, **kwargs):
        #set directory
        global directoryContent
        if(phase == '0'):
            directoryContent = settings.BSI_DE
        elif(phase == '1'):
            directoryContent = settings.TEMP_BSI_DE
        else:
            raise ValueError('Please set a phase with -a phase=x x = [0|1]')
        super(bsiSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print('Start Crawling the content of the BSI')
        # get all links under Bausteine, Elementare Gefährdungen und Umsetzungshinweise
        urlsG = get_links(response, 'Elementare Gefährdungen')
        urlsB = get_links(response, 'Bausteine')
        urlsU = get_links(response, 'Umsetzungshinweise')

        # go to every link
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

    def parse_following_urls_of_G(self, response):
        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1/text()').extract()[0].strip()

        h1Element = content.xpath('h1')

        allRelatedContentHTML = h1Element[0].xpath(xpathString).extract()
        allRelatedContentOneStringHTML = functools.reduce(lambda x, y: x + y, allRelatedContentHTML)

        f = open(directoryContent + '/' + directoryContentThreats + re.sub('/', '-', h1) + '.md', 'w')
        f.write(md(allRelatedContentOneStringHTML))
        f.close()

    def parse_following_urls_H(self, response):

        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1/text()').extract()[0].strip()

        h2Element = content.xpath('h2')

        allRelatedContentHTML = h2Element[1].xpath(xpathString).extract()
        allRelatedContentOneStringHTML = functools.reduce(lambda x, y: x + y, allRelatedContentHTML)

        f = open(directoryContent + '/' + directoryContentNotes + re.sub('/', '-', h1) + '.md', 'w')
        f.write(md(allRelatedContentOneStringHTML))
        f.close()

    def parse_following_urls(self, response):

        SET_SELCTOR = '#content'
        content = response.css(SET_SELCTOR)
        h1 = content.xpath('h1/text()').extract()[0].strip()

        h2Element = content.xpath('h2')

        allRelatedContentHTML = h2Element[1].xpath(xpathString).extract()
        allRelatedContentOneStringHTML = functools.reduce(lambda x, y: x + y, allRelatedContentHTML)

        f = open(directoryContent + '/' + directoryContentComponent + re.sub('/', '-', h1) + '.md', 'w')
        f.write(md(allRelatedContentOneStringHTML))
        f.close()

    def closed(self, reason):
        print('Crawler is finshed')
