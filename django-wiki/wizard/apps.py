from django.apps import AppConfig
from .wizard import generateSortedTopicList,generateElementTopics

class wizardConfig(AppConfig):
    name = 'wizard'

    def ready(self):
        generateSortedTopicList('t')
        generateSortedTopicList('c')

        generateElementTopics('t')
        generateElementTopics('c')




