from django.conf.urls import url
from .update import  Update, check_update#,performMidPhase,performPostPhase

urlpatterns = [
       # url(r'^performMidPhase/', performMidPhase),
        #url(r'^performPostPhase/', performPostPhase),
        url(r'^Update/', Update),
        url(r'^check_update/', check_update),
        ]
