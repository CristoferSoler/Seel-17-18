import argparse
import django
import configparser
import win32com.client
import os
import sys
import string
import filecmp


sys.path.append("C:/githubRepo/Seel-17-18/django-wiki")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()
from os.path import  isfile, isdir, join
from os import listdir
from wiki.models import Article, URLPath, Site, ArticleRevision
from bsiwiki import settings
from bsi.models import BSI, UGA,BSI_Article_type


txtFolderDir = './Cross_Reference_Files/'
excelFolderDir = './Cross_Reference_Tables/'
macroFileDir = './Cross Reference 2018.xlsm/'
CRF = './CRF/'
system_devices = ["APP", "SYS","IND", "CON", "ISMS", "ORP", "OPS", "DER", "NET", "INF"]
def readConfig(varname):
    configParser = configparser.RawConfigParser()
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
        doUpdate(bsiDir, update)
    else:
        doImport()

    cleanUp()


def doImport():
    # go through the dir and read the content of each file
        # if it's a component, append the threat-measures relationships
        # just in case, look in DB, find if an article with the same headerID exists
        # if it doesn't (it should always be this case)
        # then create a new article and its urlpath
        site = Site.objects.get_current()
        for dirpath, dirnames, filenames in os.walk(settings.CRAWLER_DIRECTORY):
            # check the bsi article type is a component or threat or implementation notes
            sub_article_type = os.path.basename(dirpath)
            if sub_article_type == "C":
                article_type = BSI_Article_type.COMPONENT
                parent = BSI.get_or_create_bsi_subroots("components", "BSI.components", "", "Components")
            elif sub_article_type == "N":
                article_type = BSI_Article_type.IMPLEMENTATIONNOTES
                parent = BSI.get_or_create_bsi_subroots("implementationNotes", "BSI.implementationNotes", "",
                                                        "Implementation Notes")
            elif sub_article_type == "T":
                 article_type = BSI_Article_type.THREAT
                 parent = BSI.get_or_create_bsi_subroots("threats", "BSI.threats", "", "Threats")

            for filename in [f for f in filenames if f.endswith(".md")]:
                # get the drive and the filepath
                path_and_file = os.path.join(dirpath, filename)
                # get the path and file name
                location, file = os.path.split(path_and_file)
                # get the file id and the titel
                file_name = os.path.splitext(file)[0]
                id = get_bsi_article_id(sub_article_type, file_name)

                # append the Cross reference relation files to the content
                # of each component article before import it in the database
                if sub_article_type == "C":
                    appendThreatMeasureRelation(path_and_file, id)

                # import the content to the database
                with open(path_and_file) as data_file:
                    content = data_file.readlines()
                    revision_kwargs = {'content': content, 'user_message': 'BSI article creation',
                                       'ip_address': '0.0.0.0'}
                    BSI.create(parent=parent, slug=id, title=file_name, article_type=article_type, **revision_kwargs)
                    print(file_name + " is saved")

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

def find_between( s, first, last ):
    # find the Implementation Notes id in the file name
    try:
        start = s.index(first)
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def get_bsi_article_id(type, file_name):
    # search the BSI id in the file name
    id =''
    if type == 'C':
        id = file_name.split(" ",1)[0]
    elif type == "T":
        id = "".join(file_name.split(" ", 2)[:2])
    elif type == "N":
       for n_id in system_devices:
            if n_id in file_name:
                id = find_between(file_name, n_id," ")

    return id



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


def appendThreatMeasureRelation(path_and_file, id):
    try:
        for cr_file in [f for f in listdir(CRF) if f.endswith(".md")]:
            path_and_ref = os.path.join(CRF, cr_file)
            if id in cr_file:
                with open(path_and_ref, 'r')as cr:
                    cr_data = cr.read()
                cr.close()
                with open(path_and_file, 'a') as data_file:
                    data_file.write(cr_data)
                data_file.close()
    except IOError:
        print('An error occurred trying to open (read/write) the file.')


#Calling Macro to get cross reference relation tables
def generateComponentsThreatsMeasuresRelation(excelFolderDir = excelFolderDir, macroFileDir = macroFileDir, txtFolderDir = txtFolderDir):
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Visible = True
    Path = macroFileDir
    xl.Workbooks.Open(Filename=Path)
    param1 = excelFolderDir #"C:\\Users\\Master\\Desktop\\Cross_Reference_Tables"
    param2 = txtFolderDir #"C:\\Users\\Master\\Desktop\\Cross_Reference_files"
    xl.Application.Run("Extraction", param1, param2)

def cleanUp():
    # TODO remove all temp dirs and update files in current dirs
    # We need the path to old BSI dir to update its content?
    return

def get_cr_relation():
    # extract for each component the cross reference relation
    try:
        for filename in [f for f in listdir(txtFolderDir) if f.endswith(".txt")]:
            # extract the component, threats and requirements ids from the macro files
            path_and_file = os.path.join(txtFolderDir, filename)
            with open(path_and_file) as data_file:
                componentId = data_file.readline().rstrip()
                threats_requirements_id = data_file.read().splitlines()

                # check the references folder (bsiCrawler) to append the ids
                # to the names of the threats and requirements
                # build new md files contains the CR relation
                for referencename in [r for r in listdir(settings.REFERENCE_DIRECTORY) if r.endswith(".txt")]:
                    if componentId in referencename:
                        path_and_reference = os.path.join(settings.REFERENCE_DIRECTORY, referencename)
                        reference_name = os.path.splitext(referencename)[0]
                        component_file = CRF + reference_name
                        new_component_file = open(component_file + '.md', "w+")

                        for id in threats_requirements_id:
                            with open(path_and_reference) as reference_file:
                                 for line in reference_file:
                                    if id.strip() in line:
                                        line = line.replace("####", "  *")
                                        new_component_file.write(line)
                        new_component_file.close()
    except IOError:
        print('An error occurred trying to open (read/write) the file.')


# should not be imported by other module
if __name__ == '__main__':
    #generateComponentsThreatsMeasuresRelation()
    #print( getCrossRefernceRelation())
    #get_cr_relation()
    #bsiDir, file = parseArgs()
    #setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
    #django.setup()
    #main(bsiDir, file)
    doImport()
    print("worked!")
