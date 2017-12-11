from wiki.models import URLPath
from bsiwiki import settings

def init():
    revision_kwargs = {'content': '', 'user_message': 'Initializer Service', 'ip_address': '0.0.0.0'}
    queryset_root = URLPath.objects.filter(slug=None)

    # if there is no root article, create it here
    if not queryset_root:
        root = URLPath.create_root(title="root", **revision_kwargs)
    else:
        root = queryset_root[0]

    queryset_uga_head = URLPath.objects.filter(slug='uga', parent=root)
    # if there is no uga head article, create it here
    if not queryset_uga_head:
        URLPath.create_urlpath(parent=root, slug='uga', title='User Generated Articles', **revision_kwargs)

    queryset_bsi_head = URLPath.objects.filter(slug='bsi', parent=root)
    # if there is no bsi head article, create it here
    if not queryset_bsi_head:
        URLPath.create_urlpath(parent=root, slug='bsi', title='BSI Compendium', **revision_kwargs)

    queryset_archive_head = URLPath.objects.filter(slug='archive', parent=root)
    # if archive is installed and archive head article does not exist, create it here
    if 'archive' in settings.INSTALLED_APPS and not queryset_archive_head:
        URLPath.create_urlpath(parent=root, slug='archive', title='Archive Overview', **revision_kwargs)
