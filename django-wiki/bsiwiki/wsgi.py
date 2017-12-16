"""
WSGI config for bsiwiki project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from .init import init
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bsiwiki.settings")

"""
if necessary, this init function creates a root article, uga, bsi and archive head articles (below root).
todo this is not the best place to put a startup script because dummy threads may run it over time :/
"""
init()

application = get_wsgi_application()
