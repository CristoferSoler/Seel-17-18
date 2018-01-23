import re

from django import forms
from django.forms import ModelMultipleChoiceField, HiddenInput
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from wiki import models
from wiki.core.diff import simple_merge
from wiki.editors import getEditor
from wiki.forms import _clean_slug, WikiSlugField, SearchForm, SpamProtectionMixin
from wiki.models import URLPath
from django.core.exceptions import ObjectDoesNotExist

from bsi.models import UGA, BSI


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=32,
    )
    password1 = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        required=True,
        label='Password2',
        max_length=32,
        widget=forms.PasswordInput()
    )

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

class CreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        # self.request = kwargs.get('request')
        self.urlpath_parent = URLPath.get_by_path('uga/')
        # bsi = URLPath.get_by_path('bsi/')
        # bsi = BSI.objects.all()
        # liste = []
        # for bsi_article in bsi:
        #     urlpath = bsi_article.url
        #     liste.append([urlpath, urlpath.article.current_revision.title])
        #
        # # liste.append([a.get_absolute_url(), a.get_absolute_url()])
        # self.fields['article'] = forms.MultipleChoiceField(
        #     label=pgettext_lazy('Revision comment', 'BSI'),
        #     choices=liste,
        #     widget=forms.CheckboxSelectMultiple,
        #     help_text=_("Associate with a BSI article when creating an article."),
        #     required=False)

    title = forms.CharField(label=_('Title'), )
    #slug = WikiSlugField(
    #    label=_('Slug'),
    #    help_text=_(
    #        "This will be the address where your article can be found. Use only alphanumeric characters and - or _.<br>Note: If you change the slug later on, links pointing to this article are <b>not</b> updated."),
    #    max_length=models.URLPath.SLUG_MAX_LENGTH)
    content = forms.CharField(
        label=_('Contents'),
        required=False,
        widget=getEditor().get_widget())  # @UndefinedVariable

    summary = forms.CharField(
        label=pgettext_lazy('Revision comment', 'Summary'),
        help_text=_("Write a brief message for the article's history log."),
        required=False)

    #def clean_slug(self):
    #    return _clean_slug(self.cleaned_data['slug'], self.urlpath_parent)

    def clean(self):
        super(CreateForm, self).clean()
        # self.check_spam()
        return self.cleaned_data


def get_available_links():
    # BSI.objects.all()
    # bsi = URLPath.get_by_path('bsi/')
    # children = bsi.get_children()
    # list = []
    # for child in children:
    #     art = child.get_children()
    #     for a in art:
    #         list.append([a.article.current_revision.title, a.article.current_revision.title])
    bsi = BSI.objects.all()
    # ArticleRevision.objects.filter(article=)
    # url.values("article").values("current_revision").values("title")
    return bsi


def get_links(revision):
    references = UGA.get_references_by_revision(revision)
    # list = []
    # for child in references.all():
    #     art = child.url.article
    #     list.append([art.current_revision.title, art.current_revision.title])
    return references


class ArticleMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.url.article.current_revision.title


class AddLinksForm(forms.Form):
    links = ArticleMultipleChoiceField(
        label=pgettext_lazy('Revision comment', 'BSI'),
        queryset=get_available_links(),
        widget=forms.CheckboxSelectMultiple,
        help_text=_("Associate with a BSI article when creating an article"),
        required=False)

    def __init__(self, *args, **kwargs):
        super(AddLinksForm, self).__init__(*args, **kwargs)


class UGEditForm(forms.Form, SpamProtectionMixin):
    title = forms.CharField(label=_('Title'), )
    content = forms.CharField(
        label=_('Contents'),
        required=False,
        widget=getEditor().get_widget())  # @UndefinedVariable

    summary = forms.CharField(
        label=_('Summary'),
        help_text=_(
            'Give a short reason for your edit, which will be stated in the revision log.'),
        required=False)

    current_revision = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput())
    # checked = forms.BooleanField(label="Reviewed", required=False)
    links = ArticleMultipleChoiceField(
        label=pgettext_lazy('Revision comment', 'BSI'),
        queryset=get_available_links(),
        widget=forms.CheckboxSelectMultiple,
        help_text=_("Linked to these BSI articles"),
        required=False)

    def __init__(self, request, current_revision, checked, *args, **kwargs):
        self.no_clean = kwargs.pop('no_clean', False)
        self.preview = kwargs.pop('preview', False)
        self.request = request
        self.initial_revision = current_revision
        self.presumed_revision = None

        if current_revision:
            initial = {'content': current_revision.content,
                       'title': current_revision.title,
                       'current_revision': current_revision.id,
                       'checked': checked,
                       'links': UGA.get_references_by_revision(current_revision)}
            initial.update(kwargs.get('initial', {}))

            # Manipulate any data put in args[0] such that the current_revision
            # is reset to match the actual current revision.
            data = None
            if len(args) > 0:
                data = args[0]
                args = args[1:]
            if data is None:
                data = kwargs.get('data', None)
            if data:
                self.presumed_revision = data.get('current_revision', None)
                # presumed_checked = data.get('checked')
                if not str(
                        self.presumed_revision) == str(
                    self.initial_revision.id):
                    newdata = {}
                    for k, v in list(data.items()):
                        newdata[k] = v
                    newdata['current_revision'] = self.initial_revision.id
                    newdata['content'] = simple_merge(self.initial_revision.content, data.get('content', ""))
                    newdata['title'] = current_revision.title
                    newdata['links'] = UGA.get_references_by_revision(current_revision)
                    kwargs['data'] = newdata
                else:
                    # Always pass as kwarg
                    kwargs['data'] = data
                self.checked = data.get('checked')

            kwargs['initial'] = initial

        super(UGEditForm, self).__init__(*args, **kwargs)
        if self.request.user.has_perm('wiki.uncheck_article') and self.request.user.has_perm('wiki.check_article'):
            self.fields['checked'] = forms.BooleanField(label="Reviewed", required=False)
        else:
            self.fields['checked'] = forms.BooleanField(label="Reviewed", required=False, widget=HiddenInput)

    def clean_title(self):
        title = self.cleaned_data.get('title', None)
        title = (title or "").strip()
        if not title:
            raise forms.ValidationError(ugettext('Article is missing title or has an invalid title'))
        return title

    def clean(self):
        """Validates form data by checking for the following
        No new revisions have been created since user attempted to edit
        Revision title or content has changed
        """
        cd = self.cleaned_data
        if self.no_clean or self.preview:
            return cd
        if not str(self.initial_revision.id) == str(self.presumed_revision):
            raise forms.ValidationError(
                ugettext(
                    'While you were editing, someone else changed the revision. Your contents have been automatically merged with the new contents. Please review the text below.'))
        if ('title' in cd) and cd['title'] == self.initial_revision.title and cd[
            'content'] == self.initial_revision.content and ('checked' in cd) and cd['checked'] == self.initial.get(
            "checked") and cd['links'] == self.initial.get('links'):
            raise forms.ValidationError(
                ugettext('No changes made. Nothing to save.'))
        self.check_spam()
        return cd


class FilterForm(SearchForm):
    f = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'search-query'}),
        required=True)
