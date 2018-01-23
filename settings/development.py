import socket

from .base import *


SECRET_KEY = config('DJANGO_SECRET_KEY',
                    default='%D8n?HDe.e{=q[O}Ld(20K(x?!G&#4vH`hf0?;c|(#Dc%~kY}n')

DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1']

TEST_RUNNER = 'vanhack_forum.runner.PytestTestRunner'

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = config('DJANGO_EMAIL_BACKEND',
                       default='django.core.mail.backends.console.EmailBackend')

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

# enable django-debug-toolbar inside docker
if config('USE_DOCKER', default=False, cast=bool):
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + '1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


DATABASES = {
    'default': dj_database_url.config(default={
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    })
}

# ease password strength in development env
AUTH_PASSWORD_VALIDATORS = []
