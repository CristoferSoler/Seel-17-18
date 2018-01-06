from django.conf.urls import url
from .update import performMidPhase,performPostPhase

urlpatterns = [
        url(r'^performMidPhase/', performMidPhase),
        url(r'^performPostPhase/', performPostPhase),
        ]
