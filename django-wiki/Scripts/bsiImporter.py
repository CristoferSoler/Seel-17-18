import argparse
import django
import configparser
import sys
from os.path import isdir, join, isfile, basename, split, splitext
from os import listdir, environ, walk
import pdb
from datetime import datetime

sys.path.append(r'..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings
from bsi.models.article_extensions import BSI, BSI_Article_type
from wiki.models import URLPath, ArticleRevision, Article
from archive.models import Archive, ArchiveTransaction
from Scripts import Cross_References
from django.contrib.sites.models import Site


new_temp_bsi_folder = './../Seel-17-18/django-wiki/Scripts/mdNew'
crfDir = './../django-wiki/Scripts/CRF/'
system_devices = ["APP", "SYS", "IND", "CON", "ISMS", "ORP", "OPS", "DER", "NET", "INF"]
txtDir = './../django-wiki/Scripts/Cross_Reference_Files/'
csvDir = './../django-wiki/Scripts/Cross_Reference_Tables/'
# temporary variable for cross reference files. If set to TRUE, append CR to files, otherwise don't
# for testing, we should not append the CR everytime we run the importer, because then the files would contain 
# multiple CR
doCR = True


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
        bsi_root = BSI.get_or_create_bsi_root('')
        for dirpath, dirnames, filenames in walk(settings.CRAWLER_DIRECTORY):
            if not filenames:
                continue

            # check the bsi article type is a component or threat or implementation notes
            sub_article_type = basename(dirpath)
            if sub_article_type == "C":
                article_type = BSI_Article_type.COMPONENT
                parent = BSI.get_or_create_bsi_subroots(bsi_root, "components", "BSI.importer", "", "Components")
            elif sub_article_type == "N":
                article_type = BSI_Article_type.IMPLEMENTATIONNOTES
                parent = BSI.get_or_create_bsi_subroots(bsi_root, "implementationnotes", "BSI.importer", "",
                                                        "Implementation Notes")
            elif sub_article_type == "T":
                article_type = BSI_Article_type.THREAT
                parent = BSI.get_or_create_bsi_subroots(bsi_root, "threats", "BSI.importer", "", "Threats")
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

                # import the content to the database
                with open(path_and_file) as data_file:
                    content = data_file.read()
                    revision_kwargs = {'content': content, 'user_message': 'BSI.importer',
                                       'ip_address': '0.0.0.0'}
                    BSI.create(parent=parent, slug=id, title=file_name, article_type=article_type, **revision_kwargs)
                    print(file_name + " is saved")

        # append the Cross reference relation files to the content
        # of each component article before import it in the database
        if isdir(crfDir) and doCR:
            appendThreatMeasureRelation()

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
            new_bsi_subroot = BSI.get_or_create_bsi_subroots(new_page, "components", "BSI.importer", "", "Components")
        elif sub_article_type == "N":
            article_type = BSI_Article_type.IMPLEMENTATIONNOTES
            bsi_type = 'implementationnotes'
            new_bsi_subroot = BSI.get_or_create_bsi_subroots(new_page, "implementationnotes", "BSI.importer", "",
                                                                "Implementation Notes")
        elif sub_article_type == "T":
            article_type = BSI_Article_type.THREAT
            bsi_type = 'threat'
            new_bsi_subroot = BSI.get_or_create_bsi_subroots(new_page, "threats", "BSI.importer", "", "Threats")
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

                # import the content to the database
                with open(path_and_file) as data_file:
                    content = data_file.read()
                    revision_kwargs = {'content': content, 'user_message': 'BSI.importer',
                                       'ip_address': '0.0.0.0'}
                    BSI.create(parent=new_bsi_subroot, slug=id, title=file_name, article_type=article_type, **revision_kwargs)
                    print(new_bsi_subroot)
                    print(file_name + " " + id +" "+ bsi_type + " is saved")

    # append the Cross reference relation files to the content
    # of each component article before import it in the database
    #if isdir(crfDir) and doCR:
    #    appendThreatMeasureRelation()

    fillNewPage(modified, added, deleted, new_page)

    return


def createNewPage():
    # first check if it is already there
    # this is just sanity check, the new page should not exist
    try:
        new = URLPath.objects.get(slug='new')
    except Exception:
        # it does not exist, so create it
        root = URLPath.root()
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
    site = 'http://' + str(Site.objects.get_current()) + '/'
    bsi = BSI.get_or_create_bsi_root('')
    content = 'The following articles have been changed in the new BSI Catalogue:<br />'
    for bsi_type in new_page.get_children():
        if(bsi_type.slug == 'components'):
            bsi_parent = URLPath.objects.filter(slug='components', parent=bsi)[0]
            content += '<br />Components:<br />'
            for article in bsi_type.get_children():
                if(is_contained_in(modified, 'component', article.slug)):
                    content += '[' + article.slug + '](' + article.path + ') (modified)<br />'
                    print(content)
                elif(is_contained_in(added, 'component', article.slug)):
                    content += '[' + article.slug + '](' + article.path + ') (new)<br />'
            for del_article in deleted.get('type'):
                if(del_article.get('name') == 'component'):
                    for file in del_article.get('files'):
                        content += '[' + file.get('file') + '](' + site + URLPath.objects.get(slug=file.get('file'), parent=bsi_parent).path + ') (deleted)<br />'
        if(bsi_type.slug == 'threats'):
            bsi_parent = URLPath.objects.filter(slug='threats', parent=bsi)[0]
            content += '<br />Threats:<br />'
            for article in bsi_type.get_children():
                if(is_contained_in(modified, 'threat', article.slug)):
                    content += '[' + article.slug + '](' + article.path + ') (modified)<br />'
                elif(is_contained_in(added, 'threat', article.slug)):
                    content += '[' + article.slug + '](' + article.path + ') (new)<br />'
            for del_article in deleted.get('type'):
                if(del_article.get('name') == 'threat'):
                    for file in del_article.get('files'):
                        content += '[' + file.get('file') + '](' + site + URLPath.objects.get(slug=file.get('file'), parent=bsi_parent).path + ') (deleted)<br />'
        elif(bsi_type.slug == 'implementationnotes'):
            bsi_parent = URLPath.objects.filter(slug='implementationnotes', parent=bsi)[0]
            content += '<br />Implementation Notes:<br />'
            for article in bsi_type.get_children():
                if(is_contained_in(modified, 'implementationnotes', article.slug)):
                    content += '[' + article.slug + '](' + article.path + ') (modified)<br />'
                elif(is_contained_in(added, 'implementationnotes', article.slug)):
                    content += '[' + article.slug + '](' + article.path + ') (new)<br />'
            for del_article in deleted.get('type'):
                if(del_article.get('name') == 'implementationnotes'):
                    for file in del_article.get('files'):
                        content += '[' + file.get('file') + '](' + site + URLPath.objects.get(slug=file.get('file'), parent=bsi_parent).path + ') (deleted)<br />'
    revision = ArticleRevision()
    revision.inherit_predecessor(new_page.article)
    from markdownify import markdownify as md
    revision.content = md(content)
    new_page.article.add_revision(revision)
    print('Content of ' + new_page.path + ' is updated!')

def find_between(s, first, last):
    # find the Implementation Notes id in the file name
    try:
        start = s.index(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

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

import pdb
def post_phase(archiving_data, new_file):
        # after 30 days
        # create archive
        # move the old bsi articles with their related uga articles to archive
        # change the url of he new one to the old one
        # delete the new (change log) page

        archive = Archive.get_or_create(archiving_data)
        new = URLPath.objects.get(slug='new')
        bsi = URLPath.objects.get(slug='bsi')
        types = URLPath.objects.filter(parent=new)

        post_phase_move_deleted_articles(archive, new_file, bsi)
        #print(type)

        for new_type in types:
              if new_type.slug == "components":
                  post_phase_move_bsi(new_type=new_type, default_type= "components",old_parent = bsi, archive = archive)
              elif new_type.slug == "threats":
                   post_phase_move_bsi(new_type=new_type, default_type="threats", old_parent=bsi, archive=archive)
              elif new_type.slug == "implementationnotes":
                   post_phase_move_bsi(new_type=new_type, default_type="implementationnotes", old_parent=bsi, archive=archive)
        
        post_phase_delete_url(new)
        updateModificationTime()



def post_phase_move_bsi(new_type, default_type, old_parent, archive):
    # for each type append the new updates
    #pdb.set_trace()
    if default_type == "components":
        type_symbol = BSI_Article_type.COMPONENT
        #print(type_symbol)
    elif default_type == "threats":
        type_symbol = BSI_Article_type.THREAT
    elif default_type == "implementationnotes":
        type_symbol = BSI_Article_type.IMPLEMENTATIONNOTES

    if new_type.slug == default_type:
        bsi_type = URLPath.objects.get(parent=old_parent, slug= default_type)
        #print(bsi_type.path)
        new_articles = new_type.get_children()
        for new_article in new_articles:
            try:
                #print(new_article.path)
                old_article = URLPath.objects.get(parent=bsi_type, slug=new_article.slug)
                old_article.slug = type_symbol.label.lower()[:1] +"_" + old_article.slug
                #print(old_article.slug)
                old_article.save()
                for ancestor in Article.objects.get(pk=old_article.article.pk).ancestor_objects():
                    ancestor.article.clear_cache()
                ArchiveTransaction.create(archive, old_article).archive()
                old_article.set_cached_ancestors_from_parent(archive.archive_url)
                old_article.save()
                post_phase_move_references(archive, old_article)
            except Exception:
                # if old article not found, this means this is a newly added article
                print('old article not found')
            #print(bla1)
            for ancestor in new_article.article.ancestor_objects():
                ancestor.article.clear_cache()
            new_article.parent = bsi_type
            new_article.parent.parent = bsi_type.parent

            new_article.save()
            for ancestor in Article.objects.get(pk=new_article.article.pk).ancestor_objects():
                ancestor.article.clear_cache()
            new_article.set_cached_ancestors_from_parent(bsi_type)
            new_article.save()
            # print(new_article.parent.parent.path)
            # print(new_article.parent.path)
            # print(new_article.path)


def post_phase_move_references(archive, bsi_article):
    # move the uga articles that related to the old bsi to archive
    uga_ref = bsi_article.bsi.references.all()
    for ref in uga_ref:
        for ancestor in Article.objects.get(pk=ref.url.article.pk).ancestor_objects():
            ancestor.article.clear_cache()
        ArchiveTransaction.create(archive, ref.url).archive()
        ref.url.set_cached_ancestors_from_parent(archive.archive_url)
        ref.url.save()
        #Article.objects.get(pk=ref.url.article.pk).clear_cache()

def post_phase_move_deleted_articles(archive, new_file, bsi):
    # move the bsi deleted articles directly to archive
    modified, added, deleted = checkFileAction(new_file)
    #archives = Archive.get_or_create(archive)
    #bsi = URLPath.objects.get(slug='bsi')

    for elem in deleted.get('type'):
        if(elem.get('name') == "component"):
            bsi_type = URLPath.objects.get(parent=bsi, slug="components")
        if(elem.get('name') == "threat"):
            bsi_type = URLPath.objects.get(parent=bsi, slug="threats")
        if (elem.get('name') == "implementationnotes"):
            bsi_type = URLPath.objects.get(parent=bsi, slug="implementationnotes")

        for file in elem.get('files'):
            import pdb
            bsi_id = file.get('file')
            deleted_article = URLPath.objects.get(parent=bsi_type, slug=bsi_id)
            for ancestor in Article.objects.get(pk=deleted_article.article.pk).ancestor_objects():
                    ancestor.article.clear_cache()
            ArchiveTransaction.create(archive, deleted_article).archive()
            new = URLPath.objects.get(pk=deleted_article.pk)
            
            new.set_cached_ancestors_from_parent(archive.archive_url)
            #Article.objects.get(pk=deleted_article.article.pk).clear_cache()
            #pdb.set_trace()
            post_phase_move_references(archive, deleted_article)
            new.save()

def post_phase_delete_url(path):
    # delete the new page and its subroots
    #pdb.set_trace()
    children = path.get_children()
    #print(children)
    if children:
        for child in children:
            #print(child)
            child.article.delete()
            #print('deleted ' + child.path)
    path.article.delete()
    #return path.is_deleted()
    print("new path is deleted")

def updateModificationTime():
    # update the date for all unchange and change articles
    new_date = datetime.now()
    # new = datetime(2009, 10, 5)
    for bsi in BSI.objects.all():
        bsi.url.article.modified = new_date
        bsi.url.article.current_revision.modified = new_date
        bsi.url.article.current_revision.save()
        bsi.url.article.save()
    return

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


def appendThreatMeasureRelation():
    Cross_References.extraction(csvDir,txtDir)
    site = 'http://' + str(Site.objects.get_current()) + '/'
    #site = 'http://localhost:8000/'
    try:
        components_articles = BSI.get_articles_by_type('C')
        for cr_file in [f for f in listdir(crfDir) if f.endswith(".md")]:
            path_and_ref = join(crfDir, cr_file)
            for article in components_articles:
                cr_data = ""
                if article.slug in cr_file:
                    with open(path_and_ref, 'r')as cr:
                        cr_data_line = cr.readline().rstrip()
                        while cr_data_line:
                            if (cr_data_line.strip('* ').startswith('G')):
                                cr_data_line = Cross_References.find_BSI_threats(cr_data_line.strip("* "), site)
                            cr_data = cr_data + cr_data_line
                            article.article.current_revision.content += cr_data_line + "<br />"
                            cr_data_line = cr.readline()
                        article.article.current_revision.save()
                    cr.close()

    except IOError:
        print('An error occurred trying to open (read/write) the file.')


def cleanUp():
    # TODO remove all temp dirs and update files in current dirs
    # We need the path to old BSI dir to update its content?
    return


# should not be imported by other module
if __name__ == '__main__':
      #file = parseArgs()
      #main(file)
      #appendThreatMeasureRelation()
      #archive = Archive.get_or_create('2018-01')
      #post_phase_move_deleted_articles('2018-01','../../programming/bsiComparator/example_modified_files.txt')
      #post_phase('2018-01', '../../programming/bsiComparator/example_modified_files.txt')
      #updateModificationTime()
      #new = URLPath.objects.get(slug='new')
      #post_phase_delete_url(new)
      #print(post_phase_delete_url(new))
      #print(new)
      #components = URLPath.objects.get(slug='components', parent=new)
      #print(components.path)
      #print(components)
      print("finished!")
