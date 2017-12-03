from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from wiki.views import article
from . import ugaViews
from .views import BSISearchView

article_create_view_class = article.Create

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^create/', views.create,  name='create'),
    url(r'^login/', auth_views.login, {'template_name': 'bsi/account/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^search/', BSISearchView.as_view(), name='bsisearch'),
    url(r'ugarticles/',ugaViews.overviewUGA, name='ugarticles'),
    url(r'changePassword/', auth_views.password_change, {'template_name': 'bsi/account/accountsSettings.html'}, name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done, {'template_name': 'bsi/account/passwordChangeDone.html'}, name='password_change_done'),
   ]


