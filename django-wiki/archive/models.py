from django.db import models, IntegrityError
from wiki.models.urlpath import URLPath, transaction
from wiki.models.article import Article
from django.http import Http404


class Archive(models.Model):
    """
    An archive always has the same parent article. If an archive is created, it is to validate that the root archive exists.
    If it does not exist, it is created (see except statement in method create).
    """
    archive_url = models.ForeignKey('wiki.URLPath', verbose_name='archive',
                                       blank=False, null=False, related_name='url_of',
                                       on_delete=models.CASCADE,  unique = False,)

    @classmethod
    @transaction.atomic
    def get_or_create(cls, slug):
        rev_kwargs = {'content': '', 'user_message': 'Archive.create', 'ip_address': '0.0.0.0'}

        # parent of each archive is the root archive article
        parent = Archive.get_or_create_archive_root()

        # create archive with parent archive urlpath
        try:
            arch = Archive.objects.get(archive_url=URLPath.objects.filter(slug=slug))
        except:
            archive = URLPath.create_urlpath(parent=parent, slug=slug, title=slug, **rev_kwargs)
            arch = cls(archive_url=archive)

        # save into db
        arch.save()
        return arch

    @classmethod
    def get_archive_by_slug(cls, slug):
        archives = Archive.objects.filter(archive_url=URLPath.objects.filter(slug=slug))
        if not archives:
            raise Http404("No archive found that matches the specified slug: ", slug)
        if archives.count() > 1:
            raise IntegrityError(
                "Duplicate keys! There are " + str(archives.count()) + " archives with the same name: ", slug)
        return archives[0]

    def __str__(self):
        return self.archive_url.slug

    @classmethod
    def get_or_create_archive_root(cls):
        try:
            root = URLPath.objects.get(slug='archive')
        except URLPath.DoesNotExist:
            rev_kwargs = {'content': '', 'user_message': 'Archive.create', 'ip_address': '0.0.0.0'}
            root = URLPath.create_urlpath(parent=URLPath.objects.get(slug=None), slug='archive', title='Archive',
                                   **rev_kwargs)
        return root

class ArchiveTransaction(models.Model):
    """
    Instances of this class represent a transaction into an archive.
    All archives have the same root article with slug 'archive'.
    This class does not validate the archive that is taken for the transaction.
    Validation according to tree correctness (root -> 'archive' -> ...) has to take place in the class Archive itself.
    """
    archive_root = models.ForeignKey(Archive, verbose_name='archive parent article',
                                        blank=False, null=False, related_name='root_archive_of',
                                        on_delete=models.CASCADE, unique = False,)

    urlpath = models.ForeignKey('wiki.URLPath', verbose_name='urlpath to transfer',
                                   blank=False, null=True, related_name='urlpath_of',
                                   on_delete=models.CASCADE, unique = False, )

    @classmethod
    def create(cls, archive, urlpath):
        transaction = cls(archive_root=archive, urlpath=urlpath)
        transaction.save()
        return transaction

    @transaction.atomic
    def archive(self):
        # set archive root as new parent of the specified urlpath
        self.urlpath.parent = self.archive_root.archive_url
        self.urlpath.save()

        # Reload url path form database
        urlpath_of_archived_article = URLPath.objects.get(pk=self.urlpath.pk)

        # Use a copy of ourself (to avoid cache) and update article links again
        for ancestor in Article.objects.get(pk=urlpath_of_archived_article.article.pk).ancestor_objects():
            ancestor.article.clear_cache()

    @classmethod
    def get_path_by_slug(cls, archive_slug, article_slug):
        # try to find the URLPath, given the archive slug and the article slug
        # first check if the archive exists
        archive = Archive.get_archive_by_slug(archive_slug)
        # find all transactions with that archive as the root
        trans = ArchiveTransaction.objects.filter(archive_root=archive)
        if not trans:
            raise Http404("No archive found that matches the specified slug: " + archive_slug)
        for t in trans:
            try:
                if(t.urlpath == URLPath.objects.get(parent=archive.archive_url, slug=article_slug)):
                    return t.urlpath
            except Exception:
                continue
        raise Http404("No archived article found in " + archive_slug + " that matches the specified slug: " +
                      article_slug)

    @classmethod
    def get_all_archive_urlpaths(cls):
            arc_urlpaths = []
            archives = ArchiveTransaction.objects.prefetch_related('urlpath')
            for archive in archives:
                arc_urlpaths.append(archive.urlpath)
            return arc_urlpaths

    def __str__(self):
        return 'transaction of ' + self.urlpath.__str__() + ' into ' + self.archive_root.__str__()
