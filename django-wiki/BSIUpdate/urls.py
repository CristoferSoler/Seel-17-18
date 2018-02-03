from django.conf.urls import url
from .update import update, check_update

urlpatterns = [
        url(r'^update/', update),
        url(r'^check_update/', check_update),
]
