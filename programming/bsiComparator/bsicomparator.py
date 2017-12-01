import argparse
from os.path import isdir, join
import filecmp
import ConfigParser


def readConfig(varname):
    configParser = ConfigParser.RawConfigParser()
    configParser.read("config.cfg")
    return configParser.get('bsi', varname)


def parseArgs():
    parser = argparse.ArgumentParser('Compares BSI contents in two directories')
    parser.add_argument('oldBsiDir', metavar='D1', help='The directory containing the old BSI')
    parser.add_argument('newBsiDir', metavar='D2', help='The directory containing the new BSI')

    args = parser.parse_args()
    if((not isdir(args.oldBsiDir)) or (not isdir(args.newBsiDir))):
        raise ValueError("Both arguments have to be a valid directory path!")

    return args.oldBsiDir, args.newBsiDir


def compare(oldDir, newDir):
    modified = []

    # compare old dir with new dir
    dircomp = filecmp.dircmp(oldDir, newDir)
    # files that are only contained in the old dir means they are deleted
    deleted = dircomp.left_only
    # files that are only contained in the new dir means they are added
    added = dircomp.right_only
    # files that are contained in both dirs
    commonFiles = dircomp.common_files

    # look in the common files to find modified files
    for f in commonFiles:
        # compare both files, if they differ, it means they are modified
        if(not filecmp.cmp(join(newDir, f), join(oldDir, f))):
            modified.append(f)

    # generate a text file to store the names to the updated files
    generateTextFile(added, modified, deleted)


def generateTextFile(added, modified, deleted):
    # create or overwrite
    file = open(readConfig('comparator_output'), "w")

    modSym = readConfig('modified_symbol')
    addSym = readConfig('added_symbol')
    delSym = readConfig('deleted_symbol')

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
    oldDir, newDir = parseArgs()
    compare(oldDir, newDir)
