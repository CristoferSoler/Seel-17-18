from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^banUsers$', views.banUsers, name='banUsers'),
    url(r'^assignUsers', views.assignUsers, name='assignUsers'),

]
