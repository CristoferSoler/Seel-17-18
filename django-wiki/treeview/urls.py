from django.conf.urls import url
from .treeview import getTreeview
urlpatterns = [
        url(r'^gettreeview/', getTreeview),
        ]