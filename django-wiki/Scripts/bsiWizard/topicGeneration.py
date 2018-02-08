import os
import shutil
import warnings
from operator import itemgetter

import django
import pandas
import sys
from dariah_topics import mallet
from dariah_topics import postprocessing
from dariah_topics import preprocessing
from nltk.stem import WordNetLemmatizer

sys.path.append(r'..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings

pathToNormalStopwordList = settings.TOPICGENERATION_DIR + '/stopwordlist/en.txt'
pathToUpgradedStopwordList = settings.TOPICGENERATION_DIR + '/stopwordlist/en-upgraded.txt'
# pathToMallet = '/Users/Jonathan/Downloads/mallet-2.0.8/bin/mallet'
pathToMallet = settings.TOPICGENERATION_DIR + '/mallet-2.0.8/bin/mallet'
output = settings.TOPICGENERATION_DIR + '/output/'
lemmanizeCorpus = True


def getStopWordList():
    stopwords = [line.strip() for line in open(pathToUpgradedStopwordList, 'r', encoding='utf-8')]
    return stopwords


def readInFilesToPathList(path):
    files = os.listdir(path)
    return files


def convertMDtoTxt(path):
    files = readInFilesToPathList(path)
    for file in files:
        shutil.copyfile(path + '/' + file, pathOfTxt + file.replace('md', 'txt').replace(' Md', 'txt'))


def getNameOfFile(file):
    splitFiles = file.split('/')
    name = splitFiles[len(splitFiles)-1].replace('.txt', '')
    return name


def getSortedTopicList(topics, fileName):
    topicsCSV = topics.to_csv().splitlines()[1:]
    unsortedTopic = []
    for topic in topicsCSV:
        split = topic.split(',')
        unsortedTopic.append((split[0], float(split[1])))

    sortedTopic = sorted(unsortedTopic, key=itemgetter(1), reverse=True)
    topicNames = [fileName.replace('(\w+/)', '')]

    for topic in sortedTopic:
        topicNames.append(topic[0])

    return topicNames


def preProcessingCSV(document_topic, fileName):
    # delete to first t
    topicsOfFile = getSortedTopicList(document_topic, fileName)
    csvFile.append(topicsOfFile)


def writeToCSV(name):
    pd = pandas.DataFrame(csvFile)
    pd.to_csv(name, header=None, index=None)


def preprocessingOfFile(file):
    fileName = getNameOfFile(file)
    corpus = list(preprocessing.read_from_pathlist([file]))
    tokenizedCorpus = [list(preprocessing.tokenize(document)) for document in corpus]
    # limatize Corpus
    if (lemmanizeCorpus):
        lenCorpus = len(tokenizedCorpus[0])
        wnl = WordNetLemmatizer()
        for i in range(0, lenCorpus):
            word = tokenizedCorpus[0][i]
            lemmanizeWord = wnl.lemmatize(word)
            tokenizedCorpus[0][i] = lemmanizeWord

    documentTermMatrix = preprocessing.create_document_term_matrix(tokenizedCorpus, fileName)
    stopwords = getStopWordList()
    cleanTokenizedCorpus = list(preprocessing.remove_features(stopwords, tokenized_corpus=tokenizedCorpus))
    return cleanTokenizedCorpus, fileName


def modelCreation(cleanTokenizedCorpus, fileNames):
    Mallet = mallet.Mallet(pathToMallet)
    malletCorpus = Mallet.import_tokenized_corpus(cleanTokenizedCorpus, fileNames)
    if not os.path.exists(os.path.join(settings.TOPICGENERATION_DIR + '/tutorial_supplementals', 'mallet_output')):
        os.makedirs(os.path.join(settings.TOPICGENERATION_DIR + '/tutorial_supplementals', 'mallet_output'))

    Mallet.train_topics(malletCorpus,
                        output_topic_keys= settings.TOPICGENERATION_DIR + '/tutorial_supplementals/mallet_output/topic_keys.txt',
                        output_doc_topics= settings.TOPICGENERATION_DIR + '/tutorial_supplementals/mallet_output/doc_topics.txt',
                        num_topics=10,
                        num_iterations=5000,
                        num_top_words=1)

    topics = postprocessing.show_topics(topic_keys_file=settings.TOPICGENERATION_DIR + '/tutorial_supplementals/mallet_output/topic_keys.txt',
                                        num_keys=1)
    document_topics = postprocessing.show_document_topics(topics=topics,
                                                          doc_topics_file=settings.TOPICGENERATION_DIR + '/tutorial_supplementals/mallet_output/doc_topics.txt',
                                                          num_keys=1)

    return document_topics


def generateTopicTable():
    warnings.filterwarnings('ignore')
    files = readInFilesToPathList(path_to_corpus)

    for file in files:
        deleteAllFilesInDirectory(settings.TOPICGENERATION_DIR + '/tutorial_supplementals/mallet_output')
        cleanTokenizedCorpus, fileName = preprocessingOfFile(pathOfTxt + file)
        print(fileName)
        document_topics = modelCreation(cleanTokenizedCorpus, fileName)
        preProcessingCSV(document_topics, fileName)


def deleteAllFilesInDirectory(directory):
    try:
        for the_file in os.listdir(directory):
            file_path = os.path.join(directory, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


def addToStopwordList(words):
    with open(settings.TOPICGENERATION_DIR + '/stopwordlist/en-upgraded.txt', "a") as file:
        print(words)
        for word in words:
            file.write(word + '\n')

        file.close()


def duplicateStopwordList():
    pathStopwords = pathToNormalStopwordList.split('/')[0]
    shutil.copy(pathToNormalStopwordList, settings.TOPICGENERATION_DIR + '/stopwordlist/en-upgraded.txt')


def removingWordsAppearInEachText(directory):
    files = readInFilesToPathList(directory)

    wordsAppearInEachText = []

    exampleCounter = 0

    for file in files:
        fileWithoutStopwordsArray, fileName = preprocessingOfFile(pathOfTxt + file)
        fileWithoutStopwords = fileWithoutStopwordsArray[0]


        if('example' not in  fileWithoutStopwords):
            print(fileName)

        if (len(wordsAppearInEachText) == 0):
            wordsAppearInEachText = fileWithoutStopwords[:]
        else:
            wordsAppearInEachText = set(wordsAppearInEachText).intersection(fileWithoutStopwords)

    print(exampleCounter)
    addToStopwordList(list(wordsAppearInEachText))


def topicGeneration():
    global pathOfMd
    global pathOfTxt
    global path_to_corpus
    global csvFile

    # for removing all words which appears in each text
    duplicateStopwordList()

    # components
    csvFile = []
    pathOfMd = settings.BSI_EN + '/C'
    pathOfTxt = settings.TOPICGENERATION_DIR + '/txt/c/'
    path_to_corpus = settings.TOPICGENERATION_DIR + '/txt/c'
    convertMDtoTxt(pathOfMd)
    removingWordsAppearInEachText(settings.TOPICGENERATION_DIR + '/txt/c')
    generateTopicTable()
    writeToCSV(settings.TOPICGENERATION_DIR + "/csv/componentsTopics.csv")

    # threads
    csvFile = []
    pathOfMd = settings.BSI_EN + '/T'
    pathOfTxt = settings.TOPICGENERATION_DIR + '/txt/t/'
    path_to_corpus = settings.TOPICGENERATION_DIR + '/txt/t'
    convertMDtoTxt(pathOfMd)
    removingWordsAppearInEachText(settings.TOPICGENERATION_DIR + '/txt/t')
    generateTopicTable()
    writeToCSV(settings.TOPICGENERATION_DIR + "/csv/threadsTopics.csv")


if __name__ == "__main__":
    topicGeneration()
