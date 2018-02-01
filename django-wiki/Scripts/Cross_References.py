import csv
import django
import os
import sys
from os import listdir
from urllib.request import urlopen
import zipfile
from io import BytesIO

sys.path.append(r"..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings
from wiki.models import URLPath

CR_website_path = "https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/krt.zip?__blob=publicationFile&v=1"
local_path = settings.CR_CSV_DOWNLOAD_DIR
crfDir = settings.CRF_DIR
txtDir = settings.CR_TXT_DIR
csvDir = settings.CR_CSV_DIR


def get_CR_Tables():
    # extract the Cross References automatically from the BSI website
    try:
        cr = urlopen(CR_website_path)
        zip_ref = zipfile.ZipFile(BytesIO(cr.read()))
        zip_ref.extractall(local_path)
        zip_ref.close()
        return 0
    except Exception as e:
        print(e)
        print('Cross References files cannot be downloaded.')
        return -1


def extraction():
    # main function of extraction the cross rreference tables relations
    # read the csv files
    # parse the csvs
    # generate the *.md files from the relational files
    for filename in [f for f in listdir(csvDir) if f.endswith(".csv")]:
        path_and_file = os.path.join(csvDir, filename)
        if os.stat(path_and_file).st_size != 0:
            csv_parser(path_and_file, txtDir)
    get_cr_relation()


def csv_parser(path_and_file, newFolderPath):
    # parsing the csv files to extract the important info from it
    # threats and requirements relation for each component
    try:
        if not os.path.exists(txtDir):
            os.makedirs(txtDir)
        with open(path_and_file) as csvfile:
            rows = []
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                if row:
                    rows.append(row)
        location, file = os.path.split(path_and_file)
        file_name = os.path.splitext(file)[0]
        newDir = os.path.join(newFolderPath, file_name + ".txt")
        csv_to_txt = open(newDir, 'w+')
        componentId = rows[0][0]
        csv_to_txt.write(componentId + '\n')
        index = 0
        for i in range(len(rows[0])):
            requirements = []
            if index != i:
                threatId = rows[0][i]
                csv_to_txt.write(" " + threatId + '\n')
            for j in range(len(rows)):
                if rows[j][i] == "X":
                    if "A0" in rows[j][0]:
                        rows[j][0] = rows[j][0].replace("A0", "A")
                    requirements.append(rows[j][0])
            for requirement in requirements:
                csv_to_txt.write("  " + requirement + '\n')
        csv_to_txt.close()
    except IOError:
        print('An error occurred trying to open (read/write) the file.')


def get_cr_relation():
    # extract for each component the cross reference relation
    try:
        if not os.path.exists(crfDir):
            os.makedirs(crfDir)
        for filename in [f for f in listdir(txtDir) if f.endswith(".txt")]:
            # extract the component, threats and requirements ids from the macro files
            path_and_file = os.path.join(txtDir, filename)
            with open(path_and_file) as data_file:
                componentId = data_file.readline().rstrip()
                threats_requirements_id = data_file.read().splitlines()

                # check the references folder (bsiCrawler) to append the ids
                # to the names of the threats and requirements
                # build new md files contains the CR relation
                for referencename in [r for r in listdir(settings.REFERENCE_DIR) if r.endswith(".txt")]:
                    if componentId in referencename:
                        path_and_reference = os.path.join(settings.REFERENCE_DIR, referencename)
                        reference_name = os.path.splitext(referencename)[0]
                        component_file = os.path.join(crfDir, reference_name)
                        new_component_file = open(component_file + '.md', "w+")

                        for id in threats_requirements_id:
                            with open(path_and_reference) as reference_file:
                                for line in reference_file:
                                    if id.strip() in line:
                                        line = line.replace("####", "         *")
                                        new_component_file.write(line)
                        new_component_file.close()
    except IOError:
        print('An error occurred trying to open (read/write) the file.')


def find_BSI_threats(threatName, site):
    if(threatName):
        id = "".join(threatName.split(" ", 2)[:2])
        if(id):
            threat = URLPath.objects.get(slug=id)
            name = threat.article.current_revision.title
            path = site + threat.path
            mdThreat = "<br />" + '[' + name + '](' + path + ')\n'
    return mdThreat
