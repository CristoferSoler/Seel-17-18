from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.information, name='information'),
   url(r'_post_question$', views.post_question, name='post_q'),
   url(r'_post_answer$', views.post_answer, name='post_a'),
   url(r'_delete_question$', views.delete_question, name='delete_q'),
   url(r'_delete_answer$', views.delete_answer, name='delete_a'),
   url(r'_edit_question$', views.edit_question, name='edit_q'),
   url(r'_edit_answer$', views.edit_answer, name='edit_a'),

]
