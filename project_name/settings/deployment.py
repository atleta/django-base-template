from .base import *

import datetime

#ALLOWED_HOSTS += ['']

MINIFIED_JS = True

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Process should have write privileges, web server should have read privileges
MEDIA_ROOT = '/var/www/{{ project_name }}/media'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SITE_ID = 1
SITE_CONFIG = {
    'name': '',
    'domain': ''
}

STATIC_URL = '/backend/static/'

with open(os.path.join(PROJECT_ROOT, 'VERSION')) as f:
    GIT_REVISION, GIT_TIMESTAMP = f.readline().strip().split()

VERSION = GIT_REVISION
VERSION_TIMESTAMP = datetime.datetime.fromtimestamp(int(GIT_TIMESTAMP)) if GIT_TIMESTAMP else datetime.datetime.utcnow()
DEPLOYMENT_NAME = 'production'

RAVEN_CONFIG = {
    # Use "?verify_ssl=0" at the end of the url if you don't have a valid certificate
    'dsn': 'https://',
}

# This MUST be set to the domain names this instance is allowed to serve, otherwise
#  all requests will result in HTTP/400
#ALLOWED_HOSTS = []

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

GOOGLE_TRACKING_ID = 'UA-'
