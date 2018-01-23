from .base import *  # noqa

# SECRET CONFIGURATION
SECRET_KEY = config('DJANGO_SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS',  default=['vanhackforum.com', ], cast=Csv())

INSTALLED_APPS += ['gunicorn', ]

DATABASES['default']['CONN_MAX_AGE'] = config('CONN_MAX_AGE', default=60)

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# EMAIL
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = config('DJANGO_DEFAULT_FROM_EMAIL',
                            default='VanHack Forum <noreply@vanhackforum.com>')
EMAIL_SUBJECT_PREFIX = config('DJANGO_EMAIL_SUBJECT_PREFIX', default='[VanHack Forum]')
SERVER_EMAIL = config('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

# Anymail with Mailgun
INSTALLED_APPS += ['anymail', ]
ANYMAIL = {
    'MAILGUN_API_KEY': config('DJANGO_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': config('MAILGUN_SENDER_DOMAIN')
}
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
