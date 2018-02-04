from django.apps import AppConfig
from django.db.models.signals import post_save,pre_save


class BsiConfig(AppConfig):
    name = 'bsi'

    def ready(self):
        import bsi.signals



