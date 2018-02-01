from os.path import isdir
import filecmp
import configparser
import django
import sys
from os import environ

sys.path.append(r'../..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings

# oldDir = settings.BSI_DE
oldDir = './md'
newDir = settings.TEMP_BSI_DE


def readConfig(varname):
    configParser = configparser.RawConfigParser()
    configParser.read("config.cfg")
    return configParser.get('bsi', varname)


def compare():
    modified = []

    # compare old dir with new dir
    dircomp = filecmp.dircmp(oldDir, newDir)

    # find the common dirs
    commondirs = dircomp.common_dirs

    if(commondirs):
        for subdir in commondirs:
            newDirpath = newDir + "/" + subdir
            oldDirpath = oldDir + "/" + subdir

            if(isdir(newDirpath) and isdir(oldDirpath)):
                dircomp = filecmp.dircmp(oldDirpath, newDirpath)

                # files that are only contained in the old dir means they are deleted
                deleted = dircomp.left_only
                # files that are only contained in the new dir means they are added
                added = dircomp.right_only
                # files that are contained in both dirs
                modified = dircomp.diff_files

                # generate a text file to store the names to the updated files
                generateTextFile(subdir, added, modified, deleted)


def generateTextFile(dir, added, modified, deleted):
    # create or overwrite
    file = open(settings.COMPARATOR_OUTPUT, "a")

    modSym = readConfig('modified_symbol')
    addSym = readConfig('added_symbol')
    delSym = readConfig('deleted_symbol')
    compSym = readConfig('component_symbol')

    # first specify in which subdir the files reside
    file.write(compSym + dir + "\n")

    # modified
    file.write(modSym + "\n")
    for f in modified:
        file.write(f + "\n")

    # added
    file.write(addSym + "\n")
    for f in added:
        file.write(f + "\n")

    # deleted
    file.write(delSym + "\n")
    for f in deleted:
        file.write(f + "\n")

    file.close()


# should not be imported by other module
if __name__ == '__main__':
    compare()
