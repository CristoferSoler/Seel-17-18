import csv
import django
import os
import sys
from os import listdir
import urllib.request
import zipfile
from io import BytesIO
#import win32com.client


sys.path.append(r"..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()
from bsiwiki import settings
from wiki.models import URLPath


csvDir = '/home/ziik/Seel-17-18/django-wiki/Scripts/Cross_Reference_Tables/csv/'
txtDir = '/home/ziik/Seel-17-18/django-wiki/Scripts/Cross_Reference_Files/'
crfDir = '/home/ziik/Seel-17-18/django-wiki/Scripts/CRF/'
CR_website_path = "https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Kompendium/krt.zip?__blob=publicationFile&v=1"
local_path = "C:/githubRepo/Seel-17-18/django-wiki/Scripts/Cross_Reference_Tables/"

def get_CR_Tables(CR_website_path, local_path):
    # extract the Cross References automatically from the BSI website
    cr = urllib.request.urlopen(CR_website_path)
    zip_ref = zipfile.ZipFile(BytesIO(cr.read()))
    zip_ref.extractall(local_path)
    zip_ref.close()
    os.remove(zip_ref)

def extraction(oldFolderPath, newFolderPath):
    # main function of extraction the cross rreference tables relations
    # read the csv files
    # parse the csvs
    # generate the *.md files from the relational files
    for filename in [f for f in listdir(oldFolderPath) if f.endswith(".csv")]:
        path_and_file = os.path.join(oldFolderPath, filename)
        if os.stat(path_and_file).st_size != 0:
            csv_parser(path_and_file,newFolderPath)
    get_cr_relation(newFolderPath)

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
        newDir = newFolderPath + file_name + ".txt"
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

def get_cr_relation(newFolderPath):
    # extract for each component the cross reference relation
	# site = str(Site.objects.get_current()) + '/'
    site = 'http://localhost:8000/'

    try:
        if not os.path.exists(crfDir):
            os.makedirs(crfDir)
        for filename in [f for f in listdir(newFolderPath) if f.endswith(".txt")]:
            # extract the component, threats and requirements ids from the macro files
            path_and_file = os.path.join(newFolderPath, filename)
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
                        component_file = crfDir + reference_name
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
            mdThreat = "<br />" +'[' + name + '](' + path + ')\n'
    return mdThreat

if __name__ == '__main__':
   # extraction(csvDir,txtDir)
    #get_CR_Tables(CR_website_path, local_path)
    print("worked!")
