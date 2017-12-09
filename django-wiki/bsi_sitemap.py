import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")
django.setup()

from wiki.models import Article, URLPath, Site, ArticleRevision

# check the type of the BSI articles and if the parent exist or not (create parent)
def checkType(BSIArticleid):
        site = Site.objects.get_current()
        bsiparent = checkBSI()
        if "B" in BSIArticleid:
            if (not URLPath.objects.filter(slug="components")):
                slug = "components"
                create_new_bsi_sitemap_branch(site,bsiparent,slug,'this is components','Components')
            return URLPath.objects.filter(slug="components")[0]
        else:
            if ("B" not in BSIArticleid and "G" in BSIArticleid):
                if (not URLPath.objects.filter(slug="threats")):
                    slug = 'threats';
                    create_new_bsi_sitemap_branch(site, bsiparent, slug, 'this is threats', 'Threats')
                return URLPath.objects.filter(slug="threats")[0]
            else:
                if "B" not in BSIArticleid and "G" not in BSIArticleid and "M" in BSIArticleid:
                    if (not URLPath.objects.filter(slug="countermeasures")):
                        slug = 'countermeasures';
                        create_new_bsi_sitemap_branch(site, bsiparent, slug, 'this is countermeasures', 'CounterMeasures')
                    return URLPath.objects.filter(slug="countermeasures")[0]

# check the root if is exist
def checkRoot():
        if(not URLPath.objects.filter(slug=None)):
            content = "root"
            site = Site.objects.get_current()
            kwargs = {'content': content, 'user_message': 'rootArticle', 'ip_address': '0.0.0.0'}
            URLPath.create_root(site= site,title="Root", request=None, **kwargs)

        return URLPath.objects.filter(slug=None)[0]

# check bsi if is exist or not
def checkBSI():
        rootParent = checkRoot()
        site = Site.objects.get_current()
        if (not URLPath.objects.filter(slug='bsi')):
            slug = 'bsi';
            create_new_bsi_sitemap_branch(site, rootParent, slug, 'this is bsi', 'BSI catalog')
        return URLPath.objects.filter(slug='bsi')[0]

# generate article for each level that not built
def create_new_bsi_sitemap_branch(site, parent, slug, content, title):
    article1_kwargs = {};
    article = Article(**article1_kwargs);
    rev1_kwargs = {'content': content, 'user_message': 'build sitemap', 'ip_address': '0.0.0.0'};
    rev1 = ArticleRevision(title=title, **rev1_kwargs);
    article.add_revision(rev1, save=True);
    article.save();

    newpath = URLPath.objects.create(
        site=site,
        parent=parent,
        slug=slug,
        article=article)
    article.add_object_relation(newpath)