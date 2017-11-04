from django.contrib import admin

from .models import Checking, Responsible, ResponsibleInit, ResponsibleImpl
from .models import Component
# Register your models here.
from .models import ComponentGroup
from .models import Countermeasure
from .models import CountermeasureCatalogue
from .models import LifecyclePhase
from .models import Role
from .models import Threat
from .models import ThreatCatalogue

admin.site.register(ComponentGroup)
admin.site.register(Component)
admin.site.register(ThreatCatalogue)
admin.site.register(Threat)
admin.site.register(CountermeasureCatalogue)
admin.site.register(Countermeasure)
# admin.site.register(Responsible) # not working 'TypeError: 'ABCMeta' object is not iterable'
# admin.site.register(ResponsibleInit) # not working 'TypeError: 'ABCMeta' object is not iterable'
# admin.site.register(ResponsibleImpl) # not working 'TypeError: 'ABCMeta' object is not iterable'
admin.site.register(Checking)
admin.site.register(Role)
admin.site.register(LifecyclePhase)