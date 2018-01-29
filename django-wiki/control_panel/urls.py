from django.conf.urls import url, include
from django.contrib import admin

from control_panel.admin import user_admin_site

admin.autodiscover()

urlpatterns = [
    url(r'^', include(user_admin_site.urls))
]
