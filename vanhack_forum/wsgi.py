"""
WSGI config for vanhack_forum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

try:
    import sqreen
    sqreen.start()
except:
    None

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

application = get_wsgi_application()
