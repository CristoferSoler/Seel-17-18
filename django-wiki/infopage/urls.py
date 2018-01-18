from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^information$', views.information, name='information'),

]
