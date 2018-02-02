import django
import sys
import os
from os.path import isdir, join, basename, splitext
from os import listdir, environ, walk
from datetime import datetime
from distutils.dir_util import copy_tree
import shutil

sys.path.append(r'..')
environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from bsiwiki import settings
from bsi.models.article_extensions import BSI, BSI_Article_type
from wiki.models import URLPath, ArticleRevision, Article
from archive.models import Archive, ArchiveTransaction
from Scripts import Cross_References
from django.contrib.sites.models import Site
from Scripts.bsiComparator.bsicomparator import readConfig
from Scripts.treeview_links import get_bsi_article_id

new_temp_bsi_folder = settings.TEMP_BSI_EN
crfDir = settings.CRF_DIR


def doImport():
    try:
        # Root article must exist!
        # go through the bsi dir
        for dirpath, dirnames, filenames in walk(settings.BSI_EN):
            if not filenames:
                continue

            # check the bsi article type is a component or threat or implementation notes
            article_type, bsi_type, parent, flag = checkBSItype(basename(dirpath), BSI.get_or_create_bsi_root(''))
            if not flag:
                continue

            # read the content of each file
            for filename in [f for f in filenames if f.endswith(".md")]:
                # get the article id and the title
                file_name = splitext(filename)[0]
                id = get_bsi_article_id(file_name)

                # import the content to the database
                with open(join(dirpath, filename)) as data_file:
                    try:
                        addToDB(data_file.read(), parent, id, filename, article_type)
                    except Exception:
                        print("Article with the ID " + id + " already exists in the DB. Skipped...")
                        continue

        # append the Cross reference files to the content
        # of each component article
        appendThreatMeasureRelation()
        cleanUp()
    except Exception as e:
        print(e)
        print("An error has occurred. Import process aborted.")


def checkBSItype(article_type, root):
    if article_type == "C":
        article_type = BSI_Article_type.COMPONENT
        bsi_type = 'component'
        parent = BSI.get_or_create_bsi_subroots(root, "components", "BSI.importer", "", "Components")
    elif article_type == "N":
        article_type = BSI_Article_type.IMPLEMENTATIONNOTES
        bsi_type = 'implementationnotes'
        parent = BSI.get_or_create_bsi_subroots(root, "implementationnotes", "BSI.importer", "",
                                                "Implementation Notes")
    elif article_type == "T":
        article_type = BSI_Article_type.THREAT
        bsi_type = 'threat'
        parent = BSI.get_or_create_bsi_subroots(root, "threats", "BSI.importer", "", "Threats")
    else:
        return None, None, None, False
    return article_type, bsi_type, parent, True


def addToDB(content, parent, id, filename, articletype):
    revision_kwargs = {'content': content, 'user_message': 'BSI.importer',
                       'ip_address': '0.0.0.0'}
    BSI.create(parent=parent, slug=id, title=filename, article_type=articletype,
               **revision_kwargs)
    print(filename + " is saved")


def doUpdate():
    # find out which files should be m/a/d
    modified, added, deleted = checkFileAction()
    new_page = createNewPage()

    # go through the dir and read the content of each file
    for dirpath, dirnames, filenames in walk(new_temp_bsi_folder):
        if not filenames:
            continue

        # check the bsi article type is a component or threat or implementation notes
        article_type, bsi_type, parent, flag = checkBSItype(basename(dirpath), new_page)
        if not flag:
            continue

        for filename in [f for f in filenames if f.endswith(".md")]:
            # get the article id and the title
            file_name = splitext(filename)[0]
            id = get_bsi_article_id(file_name)

            # if the file is new or modified, add to database under /new
            if(is_contained_in(modified, bsi_type, id) or is_contained_in(added, bsi_type, id)):
                # import the content to the database
                with open(join(dirpath, filename)) as data_file:
                    try:
                        addToDB(data_file.read(), parent, id, filename, article_type)
                    except Exception:
                        print("Article with the ID " + id + " has already been saved under \
                            the What's New page. Skipped...")
                        continue

    # appendThreatMeasureRelation()
    fillNewPage(modified, added, deleted, new_page)
    cleanUp()
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


def post_phase(archiving_data):
        # after 30 days
        # create archive
        # move the old bsi articles with their related uga articles to archive
        # change the url of he new one to the old one
        # delete the new (change log) page

        archive = Archive.get_or_create(archiving_data)
        new = URLPath.objects.get(slug='new')
        bsi = URLPath.objects.get(slug='bsi')
        types = URLPath.objects.filter(parent=new)

        post_phase_move_deleted_articles(archive, bsi)

        for new_type in types:
                if new_type.slug == "components":
                    post_phase_move_bsi(new_type=new_type, default_type="components", old_parent=bsi, archive=archive)
                elif new_type.slug == "threats":
                    post_phase_move_bsi(new_type=new_type, default_type="threats", old_parent=bsi, archive=archive)
                elif new_type.slug == "implementationnotes":
                    post_phase_move_bsi(new_type=new_type, default_type="implementationnotes",
                                        old_parent=bsi, archive=archive)

        post_phase_delete_url(new)
        updateModificationTime()


def post_phase_move_bsi(new_type, default_type, old_parent, archive):
    # for each type append the new updates
    if default_type == "components":
        type_symbol = BSI_Article_type.COMPONENT
    elif default_type == "threats":
        type_symbol = BSI_Article_type.THREAT
    elif default_type == "implementationnotes":
        type_symbol = BSI_Article_type.IMPLEMENTATIONNOTES

    if new_type.slug == default_type:
        bsi_type = URLPath.objects.get(parent=old_parent, slug=default_type)
        new_articles = new_type.get_children()
        for new_article in new_articles:
            try:
                old_article = URLPath.objects.get(parent=bsi_type, slug=new_article.slug)
                old_article.slug = type_symbol.label.lower()[:1] + "_" + old_article.slug
                old_article.save()
                for ancestor in Article.objects.get(pk=old_article.article.pk).ancestor_objects():
                    ancestor.article.clear_cache()
                ArchiveTransaction.create(archive, old_article).archive()
                old_article.set_cached_ancestors_from_parent(archive.archive_url)
                old_article.save()
                post_phase_move_references(archive, old_article)
            except Exception:
                # if old article not found, this means this is a newly added article
                pass

            new_article.parent = bsi_type
            new_article.parent.parent = bsi_type.parent
            new_article.save()
            for ancestor in Article.objects.get(pk=new_article.article.pk).ancestor_objects():
                ancestor.article.clear_cache()
            new_article.set_cached_ancestors_from_parent(bsi_type)
            new_article.save()


def post_phase_move_references(archive, bsi_article):
    # move the uga articles that related to the old bsi to archive
    uga_ref = bsi_article.bsi.references.all()
    for ref in uga_ref:
        for ancestor in Article.objects.get(pk=ref.url.article.pk).ancestor_objects():
            ancestor.article.clear_cache()
        ArchiveTransaction.create(archive, ref.url).archive()
        ref.url.set_cached_ancestors_from_parent(archive.archive_url)
        ref.url.save()


def post_phase_move_deleted_articles(archive, bsi):
    # move the bsi deleted articles directly to archive
    modified, added, deleted = checkFileAction()
    for elem in deleted.get('type'):
        if(elem.get('name') == "component"):
            bsi_type = URLPath.objects.get(parent=bsi, slug="components")
        if(elem.get('name') == "threat"):
            bsi_type = URLPath.objects.get(parent=bsi, slug="threats")
        if (elem.get('name') == "implementationnotes"):
            bsi_type = URLPath.objects.get(parent=bsi, slug="implementationnotes")

        for file in elem.get('files'):
            bsi_id = file.get('file')
            deleted_article = URLPath.objects.get(parent=bsi_type, slug=bsi_id)
            for ancestor in Article.objects.get(pk=deleted_article.article.pk).ancestor_objects():
                    ancestor.article.clear_cache()
            ArchiveTransaction.create(archive, deleted_article).archive()
            new = URLPath.objects.get(pk=deleted_article.pk)
            new.set_cached_ancestors_from_parent(archive.archive_url)

            post_phase_move_references(archive, deleted_article)
            new.save()


def post_phase_delete_url(path):
    children = path.get_children()
    if children:
        for child in children:
            child.article.delete()
    path.article.delete()
    print("What's new path is deleted!")


def updateModificationTime():
    # update the date for all unchange and change articles
    new_date = datetime.now()
    for bsi in BSI.objects.all():
        bsi.url.article.modified = new_date
        bsi.url.article.current_revision.modified = new_date
        bsi.url.article.current_revision.save()
        bsi.url.article.save()
    return


def checkFileAction():
    filepath = settings.COMPARATOR_OUTPUT
    modified = initDict()
    added = initDict()
    deleted = initDict()

    # sanity check
    assert(filepath is not None)
    # look in the text file and check if the files shoul be m/a/d
    file = open(filepath, "r")
    currentSep1 = file.readline().rstrip()
    currentSep2 = file.readline().rstrip()

    modSym = readConfig('modified_symbol')
    addSym = readConfig('added_symbol')
    delSym = readConfig('deleted_symbol')
    compSym = readConfig('component_symbol')

    for line in file:
        line = line.rstrip()
        if(line.startswith(compSym)):
            currentSep1 = line
            continue
        if(line.startswith('%')):
            currentSep2 = line
            continue

        if(currentSep2.startswith(modSym)):
            types = modified.get('type')
        elif(currentSep2.startswith(addSym)):
            types = added.get('type')
        elif(currentSep2.startswith(delSym)):
            types = deleted.get('type')
        else:
            raise ValueError('Input file might be corrupted.')

        if(currentSep1.startswith(compSym + 'C')):
            name = 'component'
        elif(currentSep1.startswith(compSym + 'T')):
            name = 'threat'
        elif(currentSep1.startswith(compSym + 'N')):
            name = 'implementationnotes'
        else:
            raise ValueError('Input file might be corrupted.')

        obj = [c for c in types if c.get('name') == name][0]
        if obj:
            obj['files'].append({'file': get_bsi_article_id(line)})

    return modified, added, deleted


def initDict():
    return {'type': [
            {'name': 'component', 'files': []},
            {'name': 'threat', 'files': []},
            {'name': 'implementationnotes', 'files': []}]}


def appendThreatMeasureRelation():
    try:
        res = Cross_References.get_CR_Tables()
        if res == -1:
            return
        Cross_References.extraction()
        site = 'http://' + str(Site.objects.get_current()) + '/'
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
            print('An error has occurred while trying to open (read/write) the Cross Reference files. Aborted...')
    except Exception as e:
        print(e)
        print("An error has occurred during Cross Reference processing. Aborted...")


def cleanUp():
    # remove all temp dirs and update files in current dirs

    try:
        # delete old content in bsi_de
        # clearDir(settings.BSI_DE)

        # copy new content to bsi_de
        # copy_tree(settings.TEMP_BSI_DE, settings.BSI_DE)

        # delete temp_de
        # clearDir(settings.TEMP_BSI_DE)

        # delete deleted articles in bsi_en
        # deleteOldFiles()

        # copy and replace articles from temp_en to bsi_en
        # putNewFiles()

        # delete temp_en
        # clearDir(settings.TEMP_BSI_EN)

        clearDir(settings.CR_CSV_DOWNLOAD_DIR)
        clearDir(settings.CR_TXT_DIR)
        clearDir(settings.CRF_DIR)
        # clearDir(settings.REFERENCE_DIR)
    except Exception as e:
        print(e)
        print("An error has occurred during cleaning up. Aborted...")


def clearDir(path):
    if os.path.exists(path) and isdir(path):
        shutil.rmtree(path)
        os.makedirs(path)


def deleteOldFiles():
    modified, added, deleted = checkFileAction()
    for elem in deleted.get('type'):
        t = elem.get('name')
        for file in elem.get('files'):
            bsi_id = file.get('file')
            for dirpath, dirnames, filenames in walk(settings.BSI_EN):
                if not filenames:
                    continue
                if basename(dirpath) != t:
                    continue
                for f in filenames:
                    # prone to typo error
                    if bsi_id in f:
                        os.remove(f)


def putNewFiles():
    c = os.join(settings.TEMP_BSI_EN, 'C')
    n = os.join(settings.TEMP_BSI_EN, 'N')
    t = os.join(settings.TEMP_BSI_EN, 'T')

    s_c = os.join(settings.BSI_EN, 'C')
    s_n = os.join(settings.BSI_EN, 'N')
    s_t = os.join(settings.BSI_EN, 'T')

    if os.path.exists(c) and os.path.exists(s_c):
        copy_tree(c, s_c)
    if os.path.exists(n) and os.path.exists(s_n):
        copy_tree(n, s_n)
    if os.path.exists(t) and os.path.exists(s_t):
        copy_tree(t, s_t)
