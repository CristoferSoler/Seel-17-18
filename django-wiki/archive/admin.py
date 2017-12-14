from django.contrib import admin
from archive.models import Archive, ArchiveTransaction

# for testing/debugging archive, enable the admin panel like the following
admin.site.register(Archive)
admin.site.register(ArchiveTransaction)
