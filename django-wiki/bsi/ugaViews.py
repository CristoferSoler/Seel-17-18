from django.shortcuts import render
from django.utils.decorators import method_decorator
# from bsi.decorators import get_article
from wiki.decorators import get_article
from wiki.models import URLPath
from wiki.views.article import ArticleView, CreateRootView
from wiki.views.article import Create
from wiki.views.article import Edit
from wiki.views.mixins import ArticleMixin
from wiki.core.plugins import registry as plugin_registry


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


class UGArticleView(ArticleView):
    template_name = "uga/article.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super(
            ArticleView,
            self).dispatch(
            request,
            article,
            *args,
            **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['selected_tab'] = 'view'
        return ArticleMixin.get_context_data(self, **kwargs)


class UGEditView(Edit):
    template_name = "uga/edit.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.sidebar_plugins = plugin_registry.get_sidebar()
        self.sidebar = []
        return super(Edit, self).dispatch(request, article, *args, **kwargs)
