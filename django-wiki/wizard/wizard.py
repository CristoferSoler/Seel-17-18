import csv
import itertools
from collections import Counter
from operator import itemgetter
from django.http import HttpResponse
import json
from random import shuffle



def getPathOfComponent(title,pathlist):
    for el in pathlist:
        if(el['name'].lower() == title.lower()):
            return el['path']
    return ''

def generateDic(list,pathlist):
    title = list[0]
    path = getPathOfComponent(title,pathlist)
    componentDic = {'name':title,'path':path ,'topics':list[1:]}
    return componentDic

def readAndProcessCSV():
    componentsWithTopics = {'components':[]}
    with open('./bsi/static/bsi/csv/topics.csv') as f:
        pathlist =  open('./../programming/bsiCrawler/treeview/pathlist.txt')
        jsonFile = json.loads(pathlist.read())
        reader = csv.reader(f)
        for row in reader:
            dic = generateDic(row,jsonFile)
            componentsWithTopics['components'].append(dic)
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
    print(components)
    jsonFile = json.dumps(components)
    return HttpResponse(jsonFile, content_type='application/json')