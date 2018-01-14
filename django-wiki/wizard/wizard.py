import csv
import itertools
import json
from collections import Counter
from operator import itemgetter
from random import shuffle

from django.http import HttpResponse

topicAndNumber = []

pathOfComponentsCSV = './../programming/bsiWizard/csv/componentsTopics.csv'
pathOfThreadsCSV = './../programming/bsiWizard/csv/threadsTopics.csv'

numberOfRelatedElements = 5


def getPathOfElement(title, pathlist, requestParameter):
    checkPath = ''
    if (requestParameter == 'c'):
        checkPath = 'components'
    elif (requestParameter == 't'):
        checkPath = 'threats'

    for el in pathlist:
        if (el['name'].lower() == title.lower() and checkPath in el['path']):
            return el['path']
    return ''


def generateDic(list, pathlist, requestParameter):
    title = list[0]
    path = getPathOfElement(title, pathlist, requestParameter)
    componentDic = {'name': title, 'path': path, 'topics': list[1:]}
    return componentDic


def readAndProcessCSV(fileName, requestParameter):
    elementWithTopics = {'element': []}
    with open(fileName) as f:
        jsonFile = getPathList()
        reader = csv.reader(f)
        for row in reader:
            dic = generateDic(row, jsonFile, requestParameter)
            elementWithTopics['element'].append(dic)
    return elementWithTopics


def getPathList():
    pathlist = open('./../programming/bsiCrawler/treeview/pathlist.txt')
    jsonFile = json.loads(pathlist.read())
    return jsonFile


def generateElementDic(title, path):
    return {'title': title, 'path': path}


def getTopicComponent(topic):
    return {'topic': topic, 'elements': []}


def generateTopicsWithRelatedElements(topics, elements, requestParameter):
    topicsWithElements = []
    listOfAllTopics = []
    listOfAllTopicNames = []
    pathList = getPathList()

    for element in elements:
        listOfAllTopics.append(element['topics'])
        listOfAllTopicNames.append(element['name'])
    rowsOfTopicList = list(zip(*listOfAllTopics))

    for topic in topics:
        topicDic = getTopicComponent(topic)

        for row in rowsOfTopicList:
            for i in range(0, len(row)):
                if (len(topicDic['elements']) < numberOfRelatedElements):
                    if row[i] == topic:
                        title = listOfAllTopicNames[i]
                        pathOfElement = getPathOfElement(title, pathList, requestParameter)
                        topicDic['elements'].append(generateElementDic(title, pathOfElement))
                else:
                    break

        topicsWithElements.append(topicDic)

    return topicsWithElements


def filterTopicElementList(topicWithRelatedElements, name):
    return list(filter(lambda x: x['topic'] == name, topicWithRelatedElements))[0]


def orderdTopicWithTheSameNumber(topicWithRelatedElements, numberOfEachTopic):
    topicListSortedByNumber = []
    currentNumber = numberOfEachTopic[0][1]
    currentNumberTopicList = []
    for index, topicNumber in enumerate(numberOfEachTopic):
        if (topicNumber[1] == currentNumber):
            currentNumberTopicList.append(filterTopicElementList(topicWithRelatedElements, topicNumber[0]))
        else:
            if (numberOfEachTopic[index] == len(numberOfEachTopic) - 1):
                currentNumberTopicList.append(filterTopicElementList(topicWithRelatedElements, topicNumber[0]))
                break
            else:
                topicListSortedByNumber.append(currentNumberTopicList)
                currentNumber = numberOfEachTopic[index][1]
                currentNumberTopicList = []
                currentNumberTopicList.append(filterTopicElementList(topicWithRelatedElements, topicNumber[0]))

    return topicListSortedByNumber


def getListOfFrequenceOfTopic(elements, requestParameter):
    topics = []
    listOfAllTopics = []

    for element in elements:
        listOfAllTopics = itertools.chain(listOfAllTopics, element['topics'])
    listOfAllTopics = list(listOfAllTopics)
    numberOfEachTopic = list(Counter(listOfAllTopics).items())
    numberOfEachTopic = sorted(numberOfEachTopic, key=itemgetter(1), reverse=True)

    for topic in numberOfEachTopic:
        topics.append(topic[0])

    topicWithRelatedElements = generateTopicsWithRelatedElements(topics, elements, requestParameter)
    orderedTopic = orderdTopicWithTheSameNumber(topicWithRelatedElements, numberOfEachTopic)

    return orderedTopic


def randomizeTopicSerialization(topicLists):
    randomizeTopicList = []
    for topicList in topicLists:
        shuffle(topicList)
        randomizeTopicList += topicList

    return randomizeTopicList


def generateSortedTopicList(fakeRequest):
    global topicListThread
    global topicListComponent

    fileName, requestParameter = getFileName(fakeRequest)
    components = readAndProcessCSV(fileName, requestParameter)
    orderdTopicList = getListOfFrequenceOfTopic(components['element'], requestParameter)

    if (fakeRequest == 't'):
        topicListThread = orderdTopicList

    elif (fakeRequest == 'c'):
        topicListComponent = orderdTopicList
    return


def generateElementTopics(fakeRequest):
    global elementTopicThread
    global elementTopicComponent

    fileName, requestParameter = getFileName(fakeRequest)
    components = readAndProcessCSV(fileName, requestParameter)
    if (fakeRequest == 't'):
        elementTopicThread = json.dumps(components)
    elif (fakeRequest == 'c'):
        elementTopicComponent = json.dumps(components)
    return


def getSortedTopicList(request):
    requestParamter = dict(request.GET)['element'][0]

    if (requestParamter == 't'):
        randomizeTopic = randomizeTopicSerialization(topicListThread)
        randomizeTopicString = json.dumps({'sortedTopicList': randomizeTopic})
        return HttpResponse(randomizeTopicString, content_type='application/json')
    elif (requestParamter == 'c'):
        randomizeTopic = randomizeTopicSerialization(topicListComponent)
        randomizeTopicString = json.dumps({'sortedTopicList': randomizeTopic})
        return HttpResponse(randomizeTopicString, content_type='application/json')


def getElementsTopics(request):
    requestParamter = dict(request.GET)['element'][0]
    if (requestParamter == 't'):
        return HttpResponse(elementTopicThread, content_type='application/json')
    elif (requestParamter == 'c'):
        return HttpResponse(elementTopicComponent, content_type='application/json')


def getFileName(request):
    fileName = ''
    requestParameter = request
    if (requestParameter == 'c'):
        fileName = pathOfComponentsCSV
    elif (requestParameter == 't'):
        fileName = pathOfThreadsCSV
    return fileName, requestParameter
