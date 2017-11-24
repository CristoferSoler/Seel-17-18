from django.db import models
from wiki.models import Article, ArticleRevision


class BSIArticle(Article):
    """

    """
    bsi_id = models.CharField(null=False, blank=False, max_length=32)


class BSIArticleRevision(ArticleRevision):
    """

    """
    location = models.TextField(null=False, blank=False)
