from django.conf.urls import url
from . import views
urlpatterns = [
    #/model/
    url(r'^$', views.index, name = 'index'),
]