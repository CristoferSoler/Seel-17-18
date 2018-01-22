from django import template

from bsi.models.article_extensions import ArticleRevisionValidation
from bsi.models import permissions

register = template.Library()


@register.filter
def can_check(obj, user):
    """
    Takes article or related to article model.
    Check if user can moderate article.
    """
    return permissions.can_check(obj, user)


@register.filter
def can_uncheck(obj, user):
    """
    Takes article or related to article model.
    Check if user can moderate article.
    """
    return permissions.can_uncheck(obj, user)


@register.filter
def is_checked(obj):
    """
    Takes article or related to article model.
    Return article revision status.
    """
    rev = obj.current_revision
    return ArticleRevisionValidation.objects.get(revision=rev).status


@register.filter
def is_uga(url):
    return hasattr(url, 'uga')
