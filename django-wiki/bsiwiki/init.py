from wiki.models import URLPath
from bsiwiki import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def assign_all_permissions(app_label, model, group):
    content_type = ContentType.objects.get(app_label=app_label, model=model)
    # get all permssions for this model
    perms = Permission.objects.filter(content_type=content_type)
    group = Group.objects.get(name=group)

    for p in perms:
        group.permissions.add(p)

def assign_permission(group, perm_name):
    permission = Permission.objects.get(name=perm_name)
    group.permissions.add(permission)

def init():
    # set the domain
    site = Site.objects.all()[0]
    site.domain = 'it-gs.ziik.tu-berlin.de'
    # The following is not commented for testing sake
    # site.domain = 'localhost:8000'
    site.save()

    #superuser group and permissions
    superusers = User.objects.filter(is_superuser=True)
    for suser in superusers:
        if not suser.groups.filter(name='administrators').exists():
            suser.groups.add(Group.objects.get(name='administrators'))
    assign_all_permissions('bsi', 'uga', 'administrators')
    assign_all_permissions('bsi', 'bsi', 'administrators')
    assign_all_permissions('archive', 'archive', 'administrators')
    assign_all_permissions('infopage', 'answer', 'administrators')
    assign_all_permissions('infopage', 'question', 'administrators')

    #moderator group and permissions
    assign_all_permissions('bsi', 'uga', 'moderators')
    assign_all_permissions('infopage', 'answer', 'moderators')
    assign_all_permissions('infopage', 'question', 'moderators')


    #user group and permissions
    assign_all_permissions('bsi', 'uga', 'users')
    assign_all_permissions('infopage', 'answer', 'users')
    assign_all_permissions('infopage', 'question', 'users')

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
