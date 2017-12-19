from wiki.models import URLPath

from .article_extensions import UGA


def can_check(article, user):
    urlpath = URLPath.objects.get(article=article)
    return not user.is_anonymous() and user.has_perm('wiki.check_article') and UGA.objects.filter(url=urlpath)


def can_uncheck(article, user):
    urlpath = URLPath.objects.get(article=article)
    return not user.is_anonymous() and user.has_perm('wiki.uncheck_article') and UGA.objects.filter(url=urlpath)
