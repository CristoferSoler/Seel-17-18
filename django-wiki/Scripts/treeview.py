import json
import re
import os
import sys
import django

# THIS FILE IS TO BE MERGED WITH BSIIMPORTER.PY
sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()


from wiki.models import URLPath
from bsi.models.article_extensions import BSI_Article_type


system_devices = ["APP", "SYS", "IND", "CON", "ISMS", "ORP", "OPS", "DER", "NET", "INF"]
path_to_treeview = '../../programming/bsiCrawler/treeview/bsiTree.txt'
path_to_treeview_with_links = '../../programming/bsiCrawler/treeview/bsiTreeLinks.txt'


def addLinksToTreeView():
    print('Loading the tree view file ' + path_to_treeview)
    parsed = []
    try:
        with open(path_to_treeview, 'r') as handle:
            parsed = json.load(handle)
    except Exception as e:
        print(e)
        raise ValueError('Cannot load and parse the json format. Please check the tree view file.')

    if(not parsed):
        raise ValueError('Loaded json file turned up empty. Please check the tree view file.')

    # site = 'http://' + str(Site.objects.get_current()) + '/'
    site = 'http://localhost:8000/'
    for elem in parsed:
        # print json.dumps(elem, indent=4)
        text = elem.get('text')
        if(text):
            bsi_type = ''
            if('components' in text.lower()):
                bsi_type = BSI_Article_type.COMPONENT
            elif('hazard' in text.lower()):
                bsi_type = BSI_Article_type.THREAT
            elif('implementation' in text.lower()):
                bsi_type = BSI_Article_type.IMPLEMENTATIONNOTES
            else:
                raise ValueError('No correct BSI type found.')
        else:
            raise ValueError('No text found in JSON.')
        nodes = elem.get('nodes')
        if(nodes):
            parents = []
            # find in database
            if(bsi_type == BSI_Article_type.COMPONENT):
                parents = URLPath.objects.filter(slug='components')
            elif(bsi_type == BSI_Article_type.THREAT):
                parents = URLPath.objects.filter(slug='threats')
            elif(bsi_type == BSI_Article_type.IMPLEMENTATIONNOTES):
                parents = URLPath.objects.filter(slug='implementationnotes')

            if(parents):
                parent = parents[0]
                children = parent.get_children()
                elem['nodes'] = find_BSI_articles(nodes, bsi_type, children, site)

    try:
        file = open(path_to_treeview_with_links, "w")
        file.write(json.dumps(parsed, indent=4))
        file.close()
        print('Successfully wrote the new tree view file to ' + path_to_treeview_with_links)
    except Exception as e:
        print(e)
        raise IOError('Error while writing to file ' + path_to_treeview_with_links)


def find_BSI_articles(nodes, type, children, site):
    if(nodes):
        for node in nodes:
            text = node.get('text').lstrip()
            if(text):
                id = get_bsi_article_id(text)
                if(id):
                    path = ''
                    for child in children:
                        if(child.slug == id):
                            node['path'] = site + child.path
                            path = child.path
                            node['href'] = site + child.path
                    if(not path):
                        print('WARNING: Path not found for ' + id + '. Please check the DB or the tree view file.')

            node = find_BSI_articles(node.get('nodes'), type, children, site)
    return nodes


def clean(path):
    if(path.startswith('bsi/')):
        return path.replace('bsi', '')
    return path


def get_bsi_article_id(file_name):
    # search the BSI id in the file name
    match = ''
    # e.g SYS.1.2.1
    regex = r"([A-Z])+(\.[0-9]+)+"
    matchObj = re.search(regex, file_name)
    if(matchObj):
        match = matchObj.group()
    else:
        # e.g SYS1.1.1
        regex = r"([A-Z])+([0-9])(\.[0-9]+)+"
        matchObj = re.search(regex, file_name)
        if(matchObj):
            match = matchObj.group()
            match = fix_typo(match)
        else:
            # e.g G02
            regex = r"([A-Z])+([0-9]+)+"
            matchObj = re.search(regex, file_name)
            if(matchObj):
                match = matchObj.group()
                match = fix_threat_id(match)
            else:
                print('No BSI ID found in ' + file_name + '. Skipped...')
    return match


def fix_threat_id(id):
    if('.' not in id):
        regex = r"^([A-Z])([0-9])"
        id = re.sub(regex, r"\1\2.", id)
    return id


def fix_typo(id):
    regex = r"^([A-Z]+)([0-9]+)"
    id = re.sub(regex, r"\1.\2", id)
    return id


if __name__ == '__main__':
    addLinksToTreeView()

