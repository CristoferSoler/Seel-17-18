from django import forms
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from wiki.editors import getEditor
from wiki.forms import _clean_slug, SpamProtectionMixin, WikiSlugField
from wiki import models
from wiki.models import URLPath
from django.utils.translation import ugettext
from wiki.core.diff import simple_merge
from wiki.forms import EditForm

from django.utils.translation import ugettext
from wiki.core.diff import simple_merge
from wiki.forms import EditForm

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )

class CreateForm(forms.Form, SpamProtectionMixin):

    children = []
    def _init_(self, request, urlpath_parent, *args, **kwargs):
        self.request = request
        self.urlpath_parent = urlpath_parent
        global children
        initial = kwargs.get('initial')
        children = initial.get('children')
        super(CreateForm, self).__init__(*args, **kwargs)

    articles = []
    for child in children:
        articles.append((child.get_absolute_url(), child.get_pk_val()))


    title = forms.CharField(label=_('Title'),)
    slug = WikiSlugField(
        label=_('Slug'),
        help_text=_(
            "This will be the address where your article can be found. Use only alphanumeric characters and - or _.<br>Note: If you change the slug later on, links pointing to this article are <b>not</b> updated."),
        max_length=models.URLPath.SLUG_MAX_LENGTH)
    content = forms.CharField(
        label=_('Contents'),
        required=False,
        widget=getEditor().get_widget())  # @UndefinedVariable

    summary = forms.CharField(
        label=pgettext_lazy('Revision comment', 'Summary'),
        help_text=_("Write a brief message for the article's history log."),
        required=False)

    articles = forms.MultipleChoiceField(choices= articles, widget=forms.CheckboxSelectMultiple())


    def clean_slug(self):
        return _clean_slug(self.cleaned_data['slug'], self.urlpath_parent)

    def clean(self):
        super(CreateForm, self).clean()
        self.check_spam()
        return self.cleaned_data

class UGAEditForm(EditForm):
    checked = forms.BooleanField(label="Reviewed", required=False)

    def _init_(self, request, current_revision, checked, *args, **kwargs):

        self.request = request
        self.no_clean = kwargs.pop('no_clean', False)
        self.preview = kwargs.pop('preview', False)
        self.initial_revision = current_revision
        self.checked = forms.BooleanField(label="Reviewed", required=False, initial=checked)

        self.presumed_revision = None
        if current_revision:
            initial = {'content': current_revision.content,
                       'title': current_revision.title,
                       'current_revision': current_revision.id,
                       'checked': checked}
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
                    kwargs['data'] = newdata
                else:
                    # Always pass as kwarg
                    kwargs['data'] = data
                self.checked = data.get('checked')

            kwargs['initial'] = initial

        super(EditForm, self)._init_(*args, **kwargs)

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
            "checked"):
            raise forms.ValidationError(
                ugettext('No changes made. Nothing to save.'))
        self.check_spam()
        return cd

