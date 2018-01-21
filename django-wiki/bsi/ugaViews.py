import difflib
import json
import logging

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from formtools.wizard.views import SessionWizardView
from wiki import forms as wiki_forms
from wiki.core.plugins import registry as plugin_registry
from wiki.core.utils import object_to_json_response
#from wiki.decorators import get_article
from .decorators import get_article
from wiki.models import ArticleRevision, reverse
from wiki.views.article import ChangeRevisionView
from wiki.views.article import CreateRootView
from wiki.views.article import Edit, Delete, History, Preview

from bsi import forms
from bsi.models.article_extensions import BSI
from .forms import AddLinksForm, CreateForm
from bsi.models.article_extensions import UGA, ArticleRevisionValidation

log = logging.getLogger(__name__)


def overview_uga(request):
    children = UGA.get_active_children()

    return render(request, 'uga/overview_uga.html', {'articles': children})


class CreateRoot(CreateRootView):
    template_name = "uga/create-root.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateRoot, self).dispatch(request, *args, **kwargs)


FORMS = [("creation", CreateForm), ("add_links", AddLinksForm)]

TEMPLATES = {"creation": "uga/create_article_master_data.html",
             "add_links": "uga/create_article_add_links.html"}


class UGACreate(SessionWizardView):

    @method_decorator(login_required)
    @method_decorator(get_article(can_write=True, can_create=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.sidebar_plugins = plugin_registry.get_sidebar()
        self.sidebar = []
        self.urlpath = kwargs.pop('urlpath', None)
        self.article = article
        self.request = request
        return super(UGACreate, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        slug = kwargs.get('form_dict')['creation'].cleaned_data['slug']
        title = kwargs.get('form_dict')['creation'].cleaned_data['title']
        content = kwargs.get('form_dict')['creation'].cleaned_data['content']
        summary = kwargs.get('form_dict')['creation'].cleaned_data['summary']
        self.uga = UGA.create_by_request(request=self.request, article=self.article,
                                         parent=self.urlpath,
                                         slug=slug, title=title,
                                         content=content,
                                         summary=summary)
        links = kwargs.get('form_dict')['add_links'].cleaned_data['links']
        for l in links:
            bsi = BSI.objects.filter(Q(url__article__current_revision__title=l))[0]
            self.uga.add_link_to_bsi(bsi)

        return redirect(reverse('get_article', kwargs={'path': self.uga.url.path}))


def get_bsi_articles(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        bsis = BSI.objects.filter(url__article__current_revision__title__icontains=q)[:20]
        results = []
        for bsi in bsis:
            title_json = {}
            title_json['id'] = bsi.url.path
            title_json['label'] = bsi.url.article.current_revision.title
            title_json['value'] = bsi.url.article.current_revision.title
            results.append(title_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


class UGEditView(Edit):
    '''
    Depending from user rights, the form differs. Moderators and Admins get the UGAEditForm which contains the
    'Reviewed' checkbox. Normal users get the django-wiki EditForm without 'Reviewed' checkbox.
    # form_class = forms.UGAEditForm
    # form_class = forms.EditForm

    '''
    template_name = "uga/edit.html"
    form_class = forms.UGEditForm

    @method_decorator(login_required)
    @method_decorator(get_article(can_write=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.sidebar_plugins = plugin_registry.get_sidebar()
        self.sidebar = []
        self.checked = ArticleRevisionValidation.objects.get(revision=article.current_revision).status

        if request.user.has_perm('wiki.uncheck_article') and request.user.has_perm('wiki.check_article'):
            pass
            # self.form_class = forms.UGEditForm
        else:
            pass
            # self.form_class = forms.EditForm
        return super(Edit, self).dispatch(request, article, *args, **kwargs)

    def form_valid(self, form):
        """Create a new article revision when the edit form is valid
        (does not concern any sidebar forms!)."""
        revision = ArticleRevision()
        revision.inherit_predecessor(self.article)
        revision.title = form.cleaned_data['title']
        revision.content = form.cleaned_data['content']
        revision.user_message = form.cleaned_data['summary']
        revision.deleted = False
        revision.set_from_request(self.request)
        self.article.add_revision(revision)
        messages.success(
            self.request,
            _('A new revision of the article was successfully added.'))
        validation = ArticleRevisionValidation.get_or_create(revision)
        if self.request.user.has_perm('wiki.check_article') and form.checked:
            validation.check_article(self.request.user)
        elif self.request.user.has_perm('wiki.uncheck_article') and not form.checked:
            validation.uncheck_article(self.request.user)
        UGA.objects.get(Q(url__article__current_revision=revision)).set_links_to_bsi(form.cleaned_data['links'])
        return self.get_success_url()

    #
    def get_form(self, form_class=None):
        """
        Checks from querystring data that the edit form is actually being saved,
        otherwise removes the 'data' and 'files' kwargs from form initialisation.
        """
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        if self.request.POST.get(
                'save',
                '') != '1' and self.request.POST.get('preview') != '1':
            kwargs['data'] = None
            kwargs['files'] = None
            kwargs['no_clean'] = True

        form = form_class(self.request, self.article.current_revision, self.checked, **kwargs)
        return form

    def get_success_url(self):
        """Go to the article view page when the article has been saved"""
        if self.urlpath:
            return redirect("get_article", path=self.urlpath.path)
        return redirect('get_article', path="uga")


@method_decorator(login_required, name='dispatch')
class UGDeleteView(Delete):
    form_class = wiki_forms.DeleteForm
    template_name = "uga/delete.html"

    def get_form(self, form_class=None):
        form = super(Delete, self).get_form(form_class=form_class)
        # if self.article.can_moderate(self.request.user):
        #     form.fields['purge'].widget = forms.forms.CheckboxInput()
        return form

    def form_valid(self, form):
        form.cleaned_data['purge'] = True
        return super(UGDeleteView, self).form_valid(form)


class UGHistoryView(History):
    template_name = "uga/history.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super(History, self).dispatch(request, article, *args, **kwargs)


def diff(request, revision_id, other_revision_id=None):
    revision = get_object_or_404(ArticleRevision, id=revision_id)

    if not other_revision_id:
        other_revision = revision.previous_revision

    baseText = other_revision.content if other_revision else ""
    newText = revision.content

    differ = difflib.Differ(charjunk=difflib.IS_CHARACTER_JUNK)
    diff = differ.compare(baseText.splitlines(1), newText.splitlines(1))

    other_changes = []

    if not other_revision or other_revision.title != revision.title:
        other_changes.append((_('New title'), revision.title))

    return object_to_json_response(
        dict(diff=list(diff), other_changes=other_changes)
    )


class UGPreviewView(Preview):
    template_name = "uga/preview_inline.html"


class UGChangeRevisionView(ChangeRevisionView):
    permanent = False

    # @method_decorator(get_article(can_write=True, not_locked=True))
    # def dispatch(self, request, article, *args, **kwargs):
    #     self.article = article
    #     self.urlpath = kwargs.pop('kwargs', False)
    #     self.change_revision()
    #
    #     return super(
    #         ChangeRevisionView,
    #         self).dispatch(
    #         request,
    #         *args,
    #         **kwargs)

    def get_redirect_url(self, **kwargs):
        # if self.urlpath:
        #     return reverse("history", kwargs={'path': self.urlpath.path})
        # else:
        #     return reverse('history', kwargs={'article_id': self.article.id})

        return reverse("get_article", kwargs={'path': kwargs.get('urlpath')})
