from django.conf.urls import url
from .update import performUpdate, Update#,performMidPhase,performPostPhase

urlpatterns = [
       # url(r'^performMidPhase/', performMidPhase),
        #url(r'^performPostPhase/', performPostPhase),
        url(r'^Update/', Update),
        ]
