from django.conf.urls import url
from .views import getTreeview

urlpatterns = [
        url(r'^gettreeview/', getTreeview),
        ]
