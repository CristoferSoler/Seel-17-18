from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.information, name='information'),
   #url(r'_post_question$', views.post_question, name='post_q'),
   #url(r'_post_answer$', views.post_answer, name='post_a')

]
