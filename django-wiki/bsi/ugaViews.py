from django.shortcuts import render
from django.utils.decorators import method_decorator
from wiki.decorators import get_article
from wiki.models import URLPath
from wiki.views.article import ArticleView
from wiki.views.article import Dir
from wiki.views.mixins import ArticleMixin


def overview_uga(request):
    uga = URLPath.get_by_path('uga/')
    children = uga.get_children()

    return render(request, 'uga/overview_uga.html', {'articles': children})


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
