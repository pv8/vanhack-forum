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

# SECURITY CONFIGURATION
# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_CONTENT_TYPE_NOSNIFF = config('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = config('DJANGO_SECURE_SSL_REDIRECT', default=True)
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

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
