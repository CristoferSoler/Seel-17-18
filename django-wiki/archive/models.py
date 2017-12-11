from django.db import models, IntegrityError
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from wiki.decorators import get_article
from wiki.models.urlpath import URLPath, transaction
from wiki.models.article import Article
from wiki.views.mixins import ArticleMixin
from django.http import Http404
from django.db.models import Q


class Archive(models.Model):
    """
    An archive always has the same parent article. If an archive is created, it is to validate that the root archive exists.
    If it does not exist, it is created (see except statement in method create).
    """
    archive_url = models.OneToOneField('wiki.URLPath', verbose_name='archive',
                                       blank=False, null=False, related_name='url_of',
                                       on_delete=models.CASCADE, )

    @classmethod
    def get_or_create(cls, slug):
        rev_kwargs = {'content': '', 'user_message': 'Archive.create', 'ip_address': 'None'}
        try:
            URLPath.objects.get(slug='archive')
        except:
            # if root archive does not exist, it is created right here
            URLPath.create_urlpath(parent=URLPath.objects.get(slug=None), slug='archive', title='Archive',
                                   **rev_kwargs)

        # parent of each archive is the root archive article
        parent = URLPath.objects.get(slug='archive')

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

    @classmethod
    def get_archive_root(cls):
        try:
            root = URLPath.objects.get(slug='archive')
        except:
            return None
        return root

    def __str__(self):
        return self.archive_url.slug


class ArchiveTransaction(models.Model):
    """
    Instances of this class represent a transaction into an archive.
    All archives have the same root article with slug 'archive'.
    This class does not validate the archive that is taken for the transaction.
    Validation according to tree correctness (root -> 'archive' -> ...) has to take place in the class Archive itself.
    """
    archive_root = models.OneToOneField('Archive', verbose_name='archive parent article',
                                        blank=False, null=False, related_name='root_archive_of',
                                        on_delete=models.CASCADE, )

    urlpath = models.OneToOneField('wiki.URLPath', verbose_name='urlpath to transfer',
                                   blank=False, null=True, related_name='urlpath_of',
                                   on_delete=models.CASCADE, )

    @classmethod
    def create(cls, archive, urlpath):
        return cls(archive_root=archive, urlpath=urlpath)

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

    def __str__(self):
        return 'transaction of ' + self.urlpath.__str__() + ' into ' + self.archive_root.__str__()
