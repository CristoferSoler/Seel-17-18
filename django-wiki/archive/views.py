from django.utils.decorators import method_decorator
from wiki import forms
from wiki.views.article import Dir, ArticleView
from .models import Archive, ArchiveTransaction
from .decorators import get_archive_article


class ArchiveDir(Dir):
    template_name = "archive/archivelist.html"

    @method_decorator(get_archive_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):

        # temp fix
        self.filter_form = forms.DirFilterForm(request.GET)
        if self.filter_form.is_valid():
            self.query = self.filter_form.cleaned_data['query']
        else:
            self.query = None

        return super(Dir, self).dispatch(request, article, *args, **kwargs)

    def get_queryset(self):
        return super(ArchiveDir, self).get_queryset()

    def get_context_data(self, **kwargs):
        return super(ArchiveDir, self).get_context_data(**kwargs)


class ArchiveArticleView(ArticleView):

    # TODO
    template_name = "archive/article.html"

    def dispatch(self, request, article, *args, **kwargs):
        # check ArchiveTransaction here
        kwargs['path'] = ArchiveTransaction.get_path_by_slug(kwargs.get('path'), article)
        article = kwargs.get('path').article
        return super(ArticleView, self).dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(ArchiveArticleView, self).get_context_data(**kwargs)
