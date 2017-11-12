from model.models import ResponsibleInit, ResponsibleImpl, Role, Countermeasure, Checking
ResponsibleInit.objects.all().delete()
ResponsibleImpl.objects.all().delete()
Checking.objects.all().delete()
Countermeasure.objects.all().delete()
Role.objects.all().delete()
