import csv

import itertools
from collections import Counter
from operator import itemgetter
from django.http import HttpResponse
import json

from wiki.models import ArticleRevision, URLPath


def getPathOfComponent(title):
    revision = ArticleRevision.objects.filter(title=title)
    parent = URLPath.objects.get(slug='components')
    urlpath = URLPath.objects.get(parent=parent, article=revision.article)
    return urlpath.path

def generateDic(list):
    title = list[0]
    #path = getPathOfComponent(title)
    componentDic = {'name':title,'path':'placeholder','topics':list[1:]}
    return componentDic

def readAndProcessCSV():
    componentsWithTopics = {'components':[]}
    with open('./bsi/static/bsi/csv/topics.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            componentsWithTopics['components'].append(generateDic(row))
    return componentsWithTopics

def getListOfFrequenceOfTopic(components):
    topics = []
    listOfAllTopics = []
    for component in components:
        listOfAllTopics = itertools.chain(listOfAllTopics, component['topics'])
    listOfAllTopics = list(listOfAllTopics)
    numberOfEachTopic = list(Counter(listOfAllTopics).items())
    numberOfEachTopic = sorted(numberOfEachTopic, key=itemgetter(1), reverse=True)
    for topic in numberOfEachTopic:
        topics.append(topic[0])
    return topics

def getSortedTopicList(request  ):
    components = readAndProcessCSV()
    frequenceOfTopics = getListOfFrequenceOfTopic(components['components'])
    jsonFile = '{ sortedTopicList:' + json.dumps(frequenceOfTopics) + "}"
    return HttpResponse(jsonFile, content_type='application/json')

def getComponentsTopics(request):
    components = readAndProcessCSV()
    jsonFile = json.dumps(components)
    return HttpResponse(jsonFile, content_type='application/json')