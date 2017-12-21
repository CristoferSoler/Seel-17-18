import argparse
import django
import configparser
import sys
from os.path import isdir, join, isfile, basename, split, splitext
from os import listdir, environ, walk

sys.path.append(r'..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings
from bsi.models import BSI, BSI_Article_type
from wiki.models import URLPath


new_temp_bsi_folder = './mdNew'
crfDir = './CRF/'
system_devices = ["APP", "SYS", "IND", "CON", "ISMS", "ORP", "OPS", "DER", "NET", "INF"]


def readConfig(varname):
    configParser = configparser.RawConfigParser()
    configParser.read("config.cfg")
    return configParser.get('bsi', varname)


def parseArgs():
    parser = argparse.ArgumentParser('Imports new or updated BSI contents to the database')
    parser.add_argument('-u', '--update', help='Use this option only when it is an update, it should be followed by '
                        'the path to the text file containing the modified files')

    args = parser.parse_args()
    if(args.update is not None):
        if(not isfile(args.update)):
            raise ValueError("Please give a valid file path!")
        if(not args.update.endswith('txt')):
            raise ValueError("The file may only be a text file!")

    return args.update


def main(update):
    if(update):
        doUpdate(update)
    else:
        doImport()

    cleanUp()


def doImport():
        # go through the dir and read the content of each file
        # if it's a component, append the threat-measures relationships
        # just in case, look in DB, find if an article with the same headerID exists
        # if it doesn't (it should always be this case)
        # then create a new article and its urlpath
        for dirpath, dirnames, filenames in walk(settings.CRAWLER_DIRECTORY):
            if not filenames:
                continue

            # check the bsi article type is a component or threat or implementation notes
            sub_article_type = basename(dirpath)
            if sub_article_type == "C":
                article_type = BSI_Article_type.COMPONENT
                parent = BSI.get_or_create_bsi_subroots("components", "BSI.importer", "", "Components")
            elif sub_article_type == "N":
                article_type = BSI_Article_type.IMPLEMENTATIONNOTES
                parent = BSI.get_or_create_bsi_subroots("implementationnotes", "BSI.importer", "",
                                                        "Implementation Notes")
            elif sub_article_type == "T":
                article_type = BSI_Article_type.THREAT
                parent = BSI.get_or_create_bsi_subroots("threats", "BSI.importer", "", "Threats")
            else:
                continue

            for filename in [f for f in filenames if f.endswith(".md")]:
                # get the drive and the filepath
                path_and_file = join(dirpath, filename)
                # get the path and file name
                location, file = split(path_and_file)
                # get the file id and the titel
                file_name = splitext(file)[0]
                id = get_bsi_article_id(sub_article_type, file_name)

                # append the Cross reference relation files to the content
                # of each component article before import it in the database
                if sub_article_type == "C" and isdir(crfDir):
                    appendThreatMeasureRelation(path_and_file, id)

                # import the content to the database
                with open(path_and_file) as data_file:
                    content = data_file.read()
                    revision_kwargs = {'content': content, 'user_message': 'BSI.importer',
                                       'ip_address': '0.0.0.0'}
                    BSI.create(parent=parent, slug=id, title=file_name, article_type=article_type, **revision_kwargs)
                    print(file_name + " is saved")

import json
def doUpdate(file):
    # find out which files should be m/a/d
    modified, added, deleted = checkFileAction(file)
    # just to see how they look
    print(json.dumps(modified, indent=4))
    print(json.dumps(added, indent=4))
    print(json.dumps(deleted, indent=4))

    new_page = createNewPage()

    # go through the dir and read the content of each file
    for dirpath, dirnames, filenames in walk(new_temp_bsi_folder):
        if not filenames:
            continue

        sub_article_type = basename(dirpath)
        if sub_article_type == "C":
            article_type = BSI_Article_type.COMPONENT
            bsi_type = 'component'
        elif sub_article_type == "N":
            article_type = BSI_Article_type.IMPLEMENTATIONNOTES
            bsi_type = 'implementationnotes'
        elif sub_article_type == "T":
            article_type = BSI_Article_type.THREAT
            bsi_type = 'threat'
        else:
            continue

        for filename in [f for f in filenames if f.endswith(".md")]:
            # get the drive and the filepath
            path_and_file = join(dirpath, filename)
            # get the path and file name
            location, file = split(path_and_file)
            # get the file id and the titel
            file_name = splitext(file)[0]
            id = get_bsi_article_id(sub_article_type, file_name)
            # if the file is new or modified, add to database under /new
            if(is_contained_in(modified, bsi_type, id) or is_contained_in(added, bsi_type, id)):
                if sub_article_type == "C" and isdir(crfDir):
                    appendThreatMeasureRelation(path_and_file, id)

                # import the content to the database
                with open(path_and_file) as data_file:
                    content = data_file.read()
                    revision_kwargs = {'content': content, 'user_message': 'BSI.importer',
                                       'ip_address': '0.0.0.0'}
                    BSI.create(parent=new_page, slug=id, title=file_name, article_type=article_type, **revision_kwargs)
                    print(file_name + " is saved")

    fillNewPage(modified, added, deleted, new_page)

    return


def createNewPage():
    # first check if it is already there
    # this is just sanity check, the new page should not exist
    try:
        new = URLPath.objects.get(slug='new')
    except URLPath.DoesNotExist:
        # it does not exist, so create it
        root = URLPath.objects.get(slug='')
        rev_kwargs = {'content': '', 'user_message': 'Importer.create', 'ip_address': '0.0.0.0'}
        new = URLPath.create_urlpath(parent=root, slug='new', title='What\'s new', **rev_kwargs)
    return new


def is_contained_in(dic, bsi_type, bsi_id):
    for elem in dic.get('type'):
        if(elem.get('name') == bsi_type):
            for file in elem.get('files'):
                if(file.get('file') == bsi_id):
                    return True
    return False


def fillNewPage(modified, added, deleted, new_page):
    # TODO
    return


def updateModificationTime():
    # TODO
    return


def find_between(s, first, last):
    # find the Implementation Notes id in the file name
    try:
        start = s.index(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def post_phase():
    # TODO
    # for unchanged articles, update its modification time
    updateModificationTime()


def get_bsi_article_id(type, file_name):
    # search the BSI id in the file name
    id = ''
    if type == 'C':
        id = file_name.split(" ", 1)[0]
    elif type == "T":
        id = "".join(file_name.split(" ", 2)[:2])
    elif type == "N":
        for n_id in system_devices:
            if n_id in file_name:
                id = find_between(file_name, n_id, " ")

    return id


def checkFileAction(filepath):
    modified = initDict()
    added = initDict()
    deleted = initDict()

    # sanity check
    assert(filepath is not None)

    # look in the text file and check if the files shoul be m/a/d
    file = open(filepath, "r")
    currentSep1 = file.readline().rstrip()
    currentSep2 = file.readline().rstrip()

    for line in file:
        line = line.rstrip()
        if(line.startswith('#')):
            currentSep1 = line
            continue
        if(line.startswith('%')):
            currentSep2 = line
            continue

        if(currentSep2.startswith('%m')):
            types = modified.get('type')
        elif(currentSep2.startswith('%a')):
            types = added.get('type')
        elif(currentSep2.startswith('%d')):
            types = deleted.get('type')
        else:
            raise ValueError('Input file might be corrupted.')

        if(currentSep1.startswith('#C')):
            name = 'component'
            sub = 'C'
        elif(currentSep1.startswith('#T')):
            name = 'threat'
            sub = 'T'
        elif(currentSep1.startswith('#N')):
            name = 'implementationnotes'
            sub = 'N'
        else:
            raise ValueError('Input file might be corrupted.')

        obj = [c for c in types if c.get('name') == name][0]
        if obj:
            obj['files'].append({'file': get_bsi_article_id(sub, line)})

    return modified, added, deleted


def initDict():
    return {'type': [
            {'name': 'component', 'files': []},
            {'name': 'threat', 'files': []},
            {'name': 'implementationnotes', 'files': []}]}


def appendThreatMeasureRelation(path_and_file, id):
    try:
        for cr_file in [f for f in listdir(crfDir) if f.endswith(".md")]:
            path_and_ref = join(crfDir, cr_file)
            if id in cr_file:
                with open(path_and_ref, 'r')as cr:
                    cr_data = cr.read()
                cr.close()
                with open(path_and_file, 'a') as data_file:
                    data_file.write(cr_data)
                data_file.close()
    except IOError:
        print('An error occurred trying to open (read/write) the file.')


def cleanUp():
    # TODO remove all temp dirs and update files in current dirs
    # We need the path to old BSI dir to update its content?
    return


# should not be imported by other module
if __name__ == '__main__':
    file = parseArgs()
    main(file)
    print("finished!")

