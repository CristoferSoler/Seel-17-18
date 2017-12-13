from dariah_topics import preprocessing
from dariah_topics import meta
from dariah_topics import mallet
from dariah_topics import postprocessing
#from dariah_topics import visualization
import warnings
import shutil
import os

pathOfMd = 'mdEn/C/'
pathOfTxt = 'txt/'
path_to_corpus = 'txt'
pathToStopwordList = 'stopwordlist/en.txt'
#pathToMallet = '/Users/Jonathan/Downloads/mallet-2.0.8/bin/mallet'
pathToMallet = 'mallet-2.0.8/bin/mallet'
output = 'output/'

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

def getNamesOfFiles(list):
    names = []
    for file in list:
        names.append(file.replace('.txt',''))
    return names

def preprocessingOfFiles():
    #get all txt files
    files = readInFilesToPathList(path_to_corpus)
    #get names of the files
    fileNames = getNamesOfFiles(files)
    #add path to files
    filesCorpus = []
    for file in files:
        filesCorpus.append(pathOfTxt + file)

    corpus = list(preprocessing.read_from_pathlist(filesCorpus))
    tokenizedCorpus = [list(preprocessing.tokenize(document)) for document in corpus]

    documentTermMatrix, document_ids, type_ids = preprocessing.create_document_term_matrix(tokenizedCorpus,
                                                                                             fileNames,
                                                                                             large_corpus=True)
    stopwords = getStopWordList()
    cleanTokenizedCorpus = list(preprocessing.remove_features(stopwords, tokenized_corpus=tokenizedCorpus))
    return cleanTokenizedCorpus, fileNames

def modelCreation(cleanTokenizedCorpus,fileNames):
    Mallet = mallet.Mallet(pathToMallet)
    malletCorpus = Mallet.import_tokenized_corpus(cleanTokenizedCorpus, fileNames)
    if not os.path.exists(os.path.join('tutorial_supplementals', 'mallet_output')):
        os.makedirs(os.path.join('tutorial_supplementals', 'mallet_output'))

    Mallet.train_topics(malletCorpus,
                        output_topic_keys= 'tutorial_supplementals/mallet_output/topic_keys.txt',
                        output_doc_topics= 'tutorial_supplementals/mallet_output/doc_topics.txt',
                        num_topics=10,
                        num_iterations=5000)
    print(malletCorpus)

def generateTopicTable():
    warnings.filterwarnings('ignore')
    cleanTokenizedCorpus, fileNames  = preprocessingOfFiles()
    modelCreation(cleanTokenizedCorpus,fileNames)

def main():
    convertMDtoTxt(pathOfMd)
    generateTopicTable()

if __name__ == "__main__":
    main()