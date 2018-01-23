from django.conf.urls import url
from .update import performUpdate#,performMidPhase,performPostPhase

urlpatterns = [
       # url(r'^performMidPhase/', performMidPhase),
        #url(r'^performPostPhase/', performPostPhase),
        url(r'^performUpdate/', performUpdate),
        ]
