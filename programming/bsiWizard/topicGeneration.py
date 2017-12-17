from operator import itemgetter
from dariah_topics import preprocessing
from dariah_topics import meta
from dariah_topics import mallet
from dariah_topics import postprocessing
from dariah_topics import visualization
import warnings
import shutil
import os
import pandas
from nltk.stem import WordNetLemmatizer
import spacy

pathOfMd = 'mdEn/C/'
pathOfTxt = 'txt/'
path_to_corpus = 'txt'
pathToStopwordList = 'stopwordlist/en.txt'
#pathToMallet = '/Users/Jonathan/Downloads/mallet-2.0.8/bin/mallet'
pathToMallet = 'mallet-2.0.8/bin/mallet'
output = 'output/'
nlp = spacy.load('en')
csvFile = []

lemmanizeCorpus = True
lemmanizeCorpus1 = False
#def lemmatizeTxt():
#    files = readInFilesToPathList(path_to_corpus)
#    for file in files:


def getStopWordList():
    stopwords = [line.strip() for line in open(pathToStopwordList, 'r', encoding='utf-8')]
    return stopwords

def readInFilesToPathList(path):
    files = os.listdir(path)
    return files

def convertMDtoTxt(path):
    files = readInFilesToPathList(path)
    for file in files:
        shutil.copyfile(pathOfMd + file,pathOfTxt + file.replace('md','txt').replace(' Md','txt'))

def getNameOfFile(file):
    name = file.replace('.txt','')
    return name

def getSortedTopicList(topics,fileName):
    topicsCSV = topics.to_csv().splitlines()[1:]
    unsortedTopic = []
    for topic in topicsCSV:
        split = topic.split(',')
        unsortedTopic.append((split[0], float(split[1])))

    sortedTopic = sorted(unsortedTopic, key=itemgetter(1), reverse=True)
    topicNames = [fileName.replace('txt/','')]
    for topic in sortedTopic:
        topicNames.append(topic[0])

    return topicNames

def preProcessingCSV(document_topic,fileName):
    #delete to first t
    topicsOfFile = getSortedTopicList(document_topic,fileName)
    csvFile.append(topicsOfFile)
    #print(csvFile)

def writeToCSV():
    pd = pandas.DataFrame(csvFile)
    pd.to_csv("csv/topics.csv")

def preprocessingOfFile(file):
    fileName = getNameOfFile(file)
    corpus = list(preprocessing.read_from_pathlist([file]))
    tokenizedCorpus = [list(preprocessing.tokenize(document)) for document in corpus]

    #print(tokenizedCorpus)

    #limatize Corpus
    if(lemmanizeCorpus):
        lenCorpus = len(tokenizedCorpus[0])
        wnl = WordNetLemmatizer()
        for i in range(0,lenCorpus):
            word = tokenizedCorpus[0][i]
            lemmanizeWord = wnl.lemmatize(word)
            tokenizedCorpus[0][i] = lemmanizeWord

    if (lemmanizeCorpus1):
        lenCorpus = len(tokenizedCorpus[0])
        #nlp = spacy.load('en')
        for i in range(0, lenCorpus):
            word = nlp(tokenizedCorpus[0][i])
            tokenizedCorpus[0][i] = word[0].lemma_
    #print(tokenizedCorpus)

    documentTermMatrix = preprocessing.create_document_term_matrix(tokenizedCorpus,fileName)
    stopwords = getStopWordList()
    cleanTokenizedCorpus = list(preprocessing.remove_features(stopwords, tokenized_corpus=tokenizedCorpus))
    return cleanTokenizedCorpus, fileName

def modelCreation(cleanTokenizedCorpus,fileNames):
    Mallet = mallet.Mallet(pathToMallet)
    malletCorpus = Mallet.import_tokenized_corpus(cleanTokenizedCorpus, fileNames)
    if not os.path.exists(os.path.join('tutorial_supplementals', 'mallet_output')):
        os.makedirs(os.path.join('tutorial_supplementals', 'mallet_output'))

    Mallet.train_topics(malletCorpus,
                        output_topic_keys= 'tutorial_supplementals/mallet_output/topic_keys.txt',
                        output_doc_topics= 'tutorial_supplementals/mallet_output/doc_topics.txt',
                        num_topics=10,
                        num_iterations=3000)
    #print(malletCorpus)

    topics = postprocessing.show_topics(topic_keys_file='tutorial_supplementals/mallet_output/topic_keys.txt')
    document_topics = postprocessing.show_document_topics(topics=topics,
                                                          doc_topics_file='tutorial_supplementals/mallet_output/doc_topics.txt', num_keys=1)

    return document_topics
    #preProcessingCSV(document_topics,fileNames)

    #print(document_topics['t'])
    #visualization.plot_doc_topics(document_topics, 0)

def generateTopicTable():
    warnings.filterwarnings('ignore')

    files = readInFilesToPathList(path_to_corpus)

    for file in files:
        cleanTokenizedCorpus, fileName  = preprocessingOfFile(pathOfTxt + file)
        print(fileName)
        document_topics = modelCreation(cleanTokenizedCorpus,fileName)
        preProcessingCSV(document_topics, fileName)

def main():
    convertMDtoTxt(pathOfMd)
    generateTopicTable()
    writeToCSV()

if __name__ == "__main__":
    main()