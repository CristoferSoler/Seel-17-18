"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from model import views

urlpatterns = [
    url(r'^admin/', admin.site.urls), # default admin handler
    url(r'^ComponentGroups/', views.ComponentGroupList.as_view()), # ComponentGroups handler
    url(r'^Component/', views.ComponentList.as_view()), # Component handler
    url(r'^ThreatCatalogue/', views.ThreatCatalogueList.as_view()), # ThreatCatalogue handler
    url(r'^Threat/', views.ThreatList.as_view()), # Threat handler
    url(r'^CountermeasureCatalogue/', views.CountermeasureCatalogueList.as_view()), #CountermeasureCatalogue handler
    url(r'^Countermeasure/', views.CountermeasureList.as_view()), # Countermeasure handler
    url(r'^Responsible/', views.ResponsibleList.as_view()), # Responsible handler
    url(r'^Role/', views.RoleList.as_view()), # Role handler
    url(r'^LifecyclePhase/', views.LifecyclePhaseList.as_view()), # LifecyclePhase handler
    url(r'^BSIArticle/', views.BSIArticleList.as_view()), # BSI article handler
]

urlpatterns = format_suffix_patterns(urlpatterns)
