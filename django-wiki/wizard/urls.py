from django.conf.urls import url
from .wizard import getSortedTopicList , getElementsTopics

urlpatterns = [
        url(r'^sortedTopics/$', getSortedTopicList),
        url(r'^elementsPlusTopics/$', getElementsTopics),
        ]