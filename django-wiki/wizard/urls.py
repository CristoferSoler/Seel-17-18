from django.conf.urls import url
from .wizard import getSortedTopicList , getComponentsTopics

urlpatterns = [
        url(r'^sortedTopics/$', getSortedTopicList),
        url(r'^componentsPlusTopics/$', getComponentsTopics),
        ]