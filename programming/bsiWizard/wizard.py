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
    clean_tokenized_corpus = list(preprocessing.remove_features(stopwords, tokenized_corpus=tokenizedCorpus))

def generateTopicTable():
    warnings.filterwarnings('ignore')
    preprocessingOfFiles()

def main():
    convertMDtoTxt(pathOfMd)
    generateTopicTable()

if __name__ == "__main__":
    main()