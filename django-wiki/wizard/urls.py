from django.conf.urls import url
from .wizard import getSortedTopicList

urlpatterns = [
        url(r'^$', getSortedTopicList),
        ]