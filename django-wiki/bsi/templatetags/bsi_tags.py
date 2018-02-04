from django import template

from bsi.models import permissions
from bsi.models.article_extensions import ArticleRevisionValidation

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


@register.filter
def is_admin(user):
    return permissions.can_add_change_delete_users(user)


@register.filter
def info_answer(user):
    return user.has_perm('infopage.add_answer')


@register.filter
def info_change_answer(user, answer):
    return user.has_perm('infopage.change_answer') or answer.user == user


@register.filter
def info_delete_answer(user, answer):
    return user.has_perm('infopage.delete_answer') or answer.user == user


@register.filter
def info_ask(user):
    return user.has_perm('infopage.add_question')


@register.filter
def info_change_question(user, question):
    return user.has_perm('infopage.change_question') or question.user == user


@register.filter
def info_delete_question(user, question):
    return user.has_perm('infopage.delete_question') or question.user == user


@register.filter
def get_path(url):
    return url.parent.path + url.slug
