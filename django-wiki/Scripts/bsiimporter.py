import argparse
import django
import configparser
import win32com.client
import os
import sys

sys.path.append("C:/githubRepo/Seel-17-18/django-wiki")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()
from os.path import  isfile, isdir, join
from os import listdir


txtFolderDir = './Cross_Reference_Files/'
excelFolderDir = './Cross_Reference_Tables/'
macroFileDir = './Cross Reference 2018.xlsm/'
def readConfig(varname):
    configParser = ConfigParser.RawConfigParser()
    configParser.read("config.cfg")
    return configParser.get('bsi', varname)


def parseArgs():
    parser = argparse.ArgumentParser('Imports new or updated BSI contents to the database')
    parser.add_argument('bsiDir', metavar='dir', help='The directory containing the BSI files to be imported')
    parser.add_argument('-u', '--update', help='Use this option only when it is an update, it should be followed by '
                        'the path to the text file containing the modified files')

    args = parser.parse_args()
    if(not isdir(args.bsiDir)):
        raise ValueError("Please give a valid directory path!")

    if(args.update is not None):
        if(not isfile(args.update)):
            raise ValueError("Please give a valid file path!")
        if(not args.update.endswith('txt')):
            raise ValueError("The file may only be a text file!")

    return args.bsiDir, args.update


def main(bsiDir, update):
    if(update):
        doUpdate(bsiDir, file)
    else:
        doImport(bsiDir)

    cleanUp()


def doImport(bsiDir):
    # go through the dir and read the content of each file
    for filename in [f for f in listdir(bsiDir) if f.lower().endswith('md')]:
        fileContent = open(join(bsiDir, filename), "r").read()

        # if it's a component, append the threat-measures relationships

        # just in case, look in DB, find if an article with the same headerID exists
        # if it doesn't (it should always be this case)
        # then create a new article and its urlpath
    return


def doUpdate(bsiDir, file):
    # find out which files should be m/a/d
    modified, added, deleted = checkFileAction(file)

    # go through the dir and read the content of each file
    for filename in [f for f in listdir(bsiDir) if f.lower().endswith('md')]:
        fileContent = open(join(bsiDir, filename), "r").read()

        # if it's a component, append the threat-measures relationships

        # for modified
        # find article, clone it, mark the clone as archive, create urlpath for the clone
        # update the content of article, do the same for user articles

        # for added
        # create new article, create its urlpath

        # for deleted
        # find article, mark it as archive, update urlpath, do the same for user articles

        # for unchanged articles, update its modification time

    return


def checkFileAction(filepath):
    modified = []
    added = []
    deleted = []

    # sanity check
    assert(filepath is not None)

    # look in the text file and check if the files shoul be m/a/d
    file = open(filepath, "r")
    currentSymbol = file.readline()
    for line in file:
        if(line.startswith('%')):
            currentSymbol = line
            continue

        if(currentSymbol == '%m'):
            modified.append(line)
        elif(currentSymbol == '%a'):
            added.append(line)
        elif(currentSymbol == '%d'):
            deleted.append(line)

    return modified, added, deleted


def appendThreatMeasureRelation(file):
    # TODO
    return


#Calling Macro to get cross reference relation tables
def generateComponentsThreatsMeasuresRelation(excelFolderDir = excelFolderDir, macroFileDir = macroFileDir, txtFolderDir = txtFolderDir):
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Visible = True
    Path = macroFileDir # "Cross Reference.xlsm"
    xl.Workbooks.Open(Filename=Path)
    param1 = excelFolderDir #"C:\\Users\\Master\\Desktop\\Cross_Reference_Tables"
    param2 = txtFolderDir #"C:\\Users\\Master\\Desktop\\Cross_Reference_files"
    xl.Application.Run("Extraction", param1, param2)

def cleanUp():
    # TODO remove all temp dirs and update files in current dirs
    # We need the path to old BSI dir to update its content?
    return


# should not be imported by other module
if __name__ == '__main__':
    #generateComponentsThreatsMeasuresRelation()
    #bsiDir, file = parseArgs()
    #setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
    #django.setup()
    #main(bsiDir, file)
    print("worked!")
