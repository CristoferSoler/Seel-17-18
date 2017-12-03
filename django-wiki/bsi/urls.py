from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from wiki.views import article
from . import ugaViews

article_create_view_class = article.Create

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^create/', views.create,  name='create'),
    url(r'^login/', auth_views.login, {'template_name': 'bsi/account/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^bsicatalog/', views.bsicatalog, name='bsicatalog'),
    url(r'^ugarticles/',ugaViews.overviewUGA, name='ugarticles')
]


