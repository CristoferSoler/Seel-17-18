import re

from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.forms import ModelMultipleChoiceField, HiddenInput
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _
from profanity import profanity
from wiki.core.diff import simple_merge
from wiki.editors import getEditor
from wiki.forms import SearchForm, SpamProtectionMixin
from wiki.models import URLPath

from bsi.models import UGA, BSI


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(
        required=True,
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        strip=False,
        # help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        required=True,
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password confirmation'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class PasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             label=_("Email"), max_length=254)

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.

        """
        active_users = get_user_model()._default_manager.filter(
            email__iexact=email, is_active=True)
        return (u for u in active_users if u.has_usable_password())

    def save(self, extra_email_context=None, domain_override=None,
             subject_template_name='bsi/registration/password_reset_subject.txt',
             email_template_name='bsi/registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }

            self.send_mail(subject_template_name, email_template_name,
                           context, from_email, user.email,
                           html_email_template_name=html_email_template_name)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        # Error password or username is invalid
        if not user:
            raise forms.ValidationError("Username or password is invalid. Please try again.")

        # banned or not activated
        if user != None and not user.is_active:
            raise forms.ValidationError("Your account is not active yet. Please checkout your mails \n"
                                        "or you are banned form the platform.")

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        required=True,
        max_length=32
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
        max_length=32,
    )
    password1 = forms.CharField(
        required=True,
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        required=True,
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype password'})
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
        raise forms.ValidationError('Passwords don\'t match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        elif profanity.contains_profanity(username):
            raise forms.ValidationError('Username is not accepted by insult detector. Please choose a different one.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


class CreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.urlpath_parent = URLPath.get_by_path('uga/')

    title = forms.CharField(label=_('Title'), )
    content = forms.CharField(
        label=_('Contents'),
        required=False,
        widget=getEditor().get_widget())  # @UndefinedVariable

    summary = forms.CharField(
        label=pgettext_lazy('Revision comment', 'Summary'),
        help_text=_("Write a brief message for the article's history log."),
        required=False)

    def clean(self):
        super(CreateForm, self).clean()
        # self.check_spam()
        return self.cleaned_data

    def clean_content(self):
        if profanity.contains_profanity(self.cleaned_data['content']):
            raise forms.ValidationError("The content is offensive.")
        return self.cleaned_data['content']

    def clean_title(self):
        if profanity.contains_profanity(self.cleaned_data['title']):
            raise forms.ValidationError("The title is offensive.")
        return self.cleaned_data['title']

    def clean_summary(self):
        if profanity.contains_profanity(self.cleaned_data['summary']):
            raise forms.ValidationError("The summary is offensive.")
        return self.cleaned_data['summary']


def get_available_links():
    # during mid phase, show only updated articles, and not the old ones
    # new articles are not shown, while deleted articles are still shown
    # because the treeview stays the same (FIXME)
    new = URLPath.objects.filter(slug='new')
    bsi_root = URLPath.objects.get(slug='bsi')
    if new:
        new_comp = URLPath.objects.filter(slug='components', parent=new[0])[0]
        new_threat = URLPath.objects.filter(slug='threats', parent=new[0])[0]
        new_impl = URLPath.objects.filter(slug='implementationnotes', parent=new[0])[0]
        new_comps = BSI.objects.filter(url__parent=new_comp)
        new_threats = BSI.objects.filter(url__parent=new_threat)
        new_impls = BSI.objects.filter(url__parent=new_impl)
        new_list = new_comps | new_threats | new_impls

        bsi_root = URLPath.objects.get(slug='bsi')
        bsi_comp_subroot = URLPath.objects.filter(slug='components', parent=bsi_root)[0]
        bsi_threat_subroot = URLPath.objects.filter(slug='threats', parent=bsi_root)[0]
        bsi_impl_subroot = URLPath.objects.filter(slug='implementationnotes', parent=bsi_root)[0]

        bsi_comps = BSI.objects.filter(url__parent=bsi_comp_subroot).exclude(url__slug__in=[e.url.slug for e in new_comps])
        bsi_threats = BSI.objects.filter(url__parent=bsi_threat_subroot).exclude(url__slug__in=[e.url.slug for e in new_threats])
        bsi_impls = BSI.objects.filter(url__parent=bsi_impl_subroot).exclude(url__slug__in=[e.url.slug for e in new_impls])
        return new_list | bsi_comps | bsi_threats | bsi_impls

    return BSI.objects.filter(url__parent__parent=bsi_root)

    # bsi = BSI.objects.all()
    # return bsi


def get_links(revision):
    references = UGA.get_references_by_revision(revision)
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

        if profanity.contains_profanity(title):
            raise forms.ValidationError(ugettext('The title is offensive.'))
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content', None)
        if profanity.contains_profanity(content):
            raise forms.ValidationError(ugettext('The content is offensive.'))
        return content

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
