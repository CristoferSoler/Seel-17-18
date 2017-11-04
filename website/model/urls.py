from django.conf.urls import url
from . import views
urlpatterns = [
    #/model/
    url(r'^$', views.index, name = 'index'),
    #/model/12/
    url(r'^(?P<id>[0-9]+)/$', views.componentGroupDetail, name = 'componentGroupDetail'),
]