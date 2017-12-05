from django.conf.urls import url
from . import views
from . import ugaViews
from django.contrib.auth import views as auth_views
from wiki.views import article
<<<<<<< HEAD
from . import ugaViews
from .views import BSISearchView
from .views import BSIArticleView
=======
>>>>>>> origin/templates

article_create_view_class = article.Create

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^(?P<path>.+/|)_create/', article_create_view_class.as_view(), {'template_name': 'bsi/create_article.html'},  name='create'),
    url(r'^login/', auth_views.login, {'template_name': 'bsi/account/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^search/', BSISearchView.as_view(), name='bsisearch'),
    url(r'^article/', BSIArticleView.as_view(), name='bsiarticle'),
    url(r'ugarticles/',ugaViews.overviewUGA, name='ugarticles'),
    url(r'changePassword/', auth_views.password_change, {'template_name': 'bsi/account/accountsSettings.html'}, name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done, {'template_name': 'bsi/account/passwordChangeDone.html'}, name='password_change_done'),
   ]
