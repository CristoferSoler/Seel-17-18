# from bsi.decorators import get_article
import logging

from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from wiki.core.plugins import registry as plugin_registry
from wiki.decorators import get_article
from wiki.models import URLPath, ArticleRevision
from wiki.views.article import Create
from wiki.views.article import CreateRootView
from wiki.views.article import Edit

from bsi import forms

log = logging.getLogger(__name__)

from bsi.models.article_extensions import UGA, ArticleRevisionValidation


def overview_uga(request):
    uga = URLPath.get_by_path('uga/')
    children = uga.get_children()

    return render(request, 'uga/overview_uga.html', {'articles': children})


class CreateRoot(CreateRootView):
    template_name = "uga/create-root.html"

    def dispatch(self, request, *args, **kwargs):
        return super(CreateRoot, self).dispatch(request, *args, **kwargs)


class UGACreate(Create):
    template_name = 'uga/create_article.html'

    @method_decorator(get_article(can_write=True, can_create=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super(Create, self).dispatch(request, article, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newpath = UGA.create_by_request(request=self.request, article=self.article,
                                                 parent=self.urlpath,
                                                 slug=form.cleaned_data['slug'], title=form.cleaned_data['title'],
                                                 content=form.cleaned_data['content'],
                                                 summary=form.cleaned_data['summary'])
            messages.success(
                self.request,
                _("New article '%s' created.") %
                self.newpath.article.current_revision.title)

        # TODO: Handle individual exceptions better and give good feedback.
        except Exception as e:
            log.exception("Exception creating article.")
            if self.request.user.is_superuser:
                messages.error(
                    self.request,
                    _("There was an error creating this article: %s") %
                    str(e))
            else:
                messages.error(
                    self.request,
                    _("There was an error creating this article."))
            return redirect('wiki:get', '')

        url = self.get_success_url()
        return url


class UGEditView(Edit):
    form_class = forms.UGAEditForm
    # form_class = forms.EditForm
    template_name = "uga/edit.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.sidebar_plugins = plugin_registry.get_sidebar()
        self.sidebar = []
        self.checked = ArticleRevisionValidation.objects.get(revision=article.current_revision).status
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
        if form.checked:
            validation.check(self.request.user)
        else:
            validation.uncheck(self.request.user)
        return self.get_success_url()

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
        return form_class(self.request, self.article.current_revision, self.checked, **kwargs)
