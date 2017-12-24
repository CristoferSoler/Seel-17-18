import csv

import itertools
from collections import Counter
from operator import itemgetter
from django.http import HttpResponse
import json
from random import shuffle
from wiki.models import ArticleRevision, URLPath


def getPathOfComponent(title):
    revision = ArticleRevision.objects.filter(title=title)
    parent = URLPath.objects.get(slug='components')
    urlpath = URLPath.objects.get(parent=parent, article=revision.article)
    return urlpath.path

def generateDic(list):
    title = list[0]
    #path = getPathOfComponent(title)
    componentDic = {'name':title,'path':'http://localhost:8000/bsi/threats/G0.1/','topics':list[1:]}
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

    #randomize the serialization of the topics regarding the intervall x>40, 40>x>20, 20>x>10, 10>x>5,x<5
    randomSerializationOfTopics = randomizeTopicSerialization(numberOfEachTopic)

    for topic in randomSerializationOfTopics:
        topics.append(topic[0])
    return topics

def randomizeTopicSerialization(topics):
    gtFourty = []
    btwFourtyAndtwenty = []
    btwTwentyAndTen = []
    btwTenAndFive = []
    smFive = []
    for topic in topics:
        countOfTopic = topic[1]
        if countOfTopic > 40:
            gtFourty.append(topic)
        if countOfTopic <= 40 and countOfTopic > 20:
            btwFourtyAndtwenty.append(topic)
        if countOfTopic <= 20 and countOfTopic > 10:
            btwTwentyAndTen.append(topic)
        if countOfTopic <= 10 and countOfTopic > 5:
            btwTenAndFive.append(topic)
        if countOfTopic <= 5:
            smFive.append(topic)
    shuffle(gtFourty)
    shuffle(btwFourtyAndtwenty)
    shuffle(btwTwentyAndTen)
    shuffle(btwTenAndFive)
    shuffle(smFive)

    randomSerializationTopics = gtFourty + btwFourtyAndtwenty +btwTwentyAndTen + btwTenAndFive + smFive

    return randomSerializationTopics


def getSortedTopicList(request  ):
    components = readAndProcessCSV()
    frequenceOfTopics = getListOfFrequenceOfTopic(components['components'])
    jsonFile = { 'sortedTopicList' : frequenceOfTopics }
    return HttpResponse(json.dumps(jsonFile), content_type='application/json')

def getComponentsTopics(request):
    components = readAndProcessCSV()
    jsonFile = json.dumps(components)
    return HttpResponse(jsonFile, content_type='application/json')