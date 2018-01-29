from django.contrib.sites.models import Site
from django.contrib import admin
from wiki.models import ArticleRevision, Article, URLPath
from wiki.plugins.images.models import Image
from wiki.plugins.attachments.models import Attachment
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.forms import UserChangeForm

class PermissionFilterMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in ('permissions', 'user_permissions'):
            qs = kwargs.get('queryset', db_field.rel.to.objects)
            qs = _filter_permissions(qs)
            kwargs['queryset'] = qs

        return super(PermissionFilterMixin, self).formfield_for_manytomany(db_field, request, **kwargs)

class MyGroupAdmin(PermissionFilterMixin, GroupAdmin):
    pass

class MyUserAdmin(PermissionFilterMixin, UserAdmin):
    pass

# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.register(User, MyUserAdmin)
# admin.site.register(Group, MyGroupAdmin)


def _filter_permissions(qs):
    return qs.exclude(codename__in=(
        # Has no admin interface:
        'add_contenttype',
        'change_contenttype',
        'delete_contenttype',

        # archive
        'add_archive',
        'delete_archive',
        'change_archive',

        'add_archivetransaction',
        'delete_archivetransaction',
        'change_archivetransaction',

        #site
        'add_site',
        'delete_site',
        'change_site',

        #settings
        'add_settings',
        'delete_settings',
        'change_settings',

        #subscription
        'add_subscription',
        'change_subscription',
        'delete_subscription',

        #article validation
        'add_articlerevisionvalidation',
        'change_articlerevisionvalidation',
        'delete_articlerevisionvalidation',

        #bsi
        'add_bsi',
        'change_bsi',
        'delete_bsi',

        #notificationType
        'add_notificationtype',
        'change_notificationtype',
        'delete_notificationtype',

        #article revision
        'add_articlerevision',
        'change_articlerevision',
        'delete_articlerevision',

        'add_session',
        'delete_session',
        'change_session',

        # django.contrib.admin
        'add_logentry',
        'change_logentry',
        'delete_logentry',

        #wikiArticle
        'add_article',
        'change_article',
        'delete_article',

        #wiki permission
        'assign',
        'grant',
        'moderate',

        #wiki plugin
        'add_articleplugin',
        'change_articleplugin',
        'delete_articleplugin',

        #wiki reusable plugin
        'add_reusableplugin',
        'change_reusableplugin',
        'delete_reusableplugin',

        #wiki revision plugin
        'add_articlerevision',
        'change_articlerevision',
        'delete_articlerevision',

        #wiki simple plugin
        'add_simpleplugin',
        'change_simpleplugin',
        'delete_simpleplugin',

        #wiki attatchment revision
        'add_attachmentrevision',
        'change_attachmentrevision',
        'delete_attachmentrevision',

        #wiki attatchment
        'add_attachment',
        'change_attachment',
        'delete_attachment',

        'add_articlesubscription',
        'change_articlesubscription',
        'delete_articlesubscription',

        #wiki image revision
        'add_imagerevision',
        'change_imagerevision',
        'delete_imagerevision',

        #wiki image
        'add_image',
        'change_image',
        'delete_image',

        #wiki article validation
        'add_articlerevisionvalidation',
        'change_articlerevisionvalidation',
        'delete_articlerevisionvalidation',

        #plugin revision
        'add_revisionplugin',
        'change_revisionplugin',
        'delete_revisionplugin',

        #wiki url path
        'add_urlpath',
        'change_urlpath',
        'delete_urlpath',
        #wiki article to object
        'add_articleforobject',
        'change_articleforobject',
        'delete_articleforobject',

        #wiki revision
        'add_revisionpluginrevision',
        'change_revisionpluginrevision',
        'delete_revisionpluginrevision',

        # sorl-thumbnail
        'add_kvstore',
        'change_kvstore',
        'delete_kvstore',
    )) \
    .exclude(codename__endswith='userobjectpermission') \
    .exclude(codename__endswith='groupobjectpermission')  # django-guardian

# admin.site.unregister(Site)
# admin.site.unregister(ArticleRevision)
# admin.site.unregister(Article)
# admin.site.unregister(URLPath)
# admin.site.unregister(Image)
# admin.site.unregister(Attachment)