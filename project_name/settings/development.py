"""
Development settings.
"""
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
WERKZEUG_DEBUG_PIN = 'off'

os.environ['WERKZEUG_DEBUG_PIN'] = WERKZEUG_DEBUG_PIN

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

try:
    with os.popen('git rev-parse --abbrev-ref HEAD') as f:
        VERSION = '[branch: %s]' % f.readline().strip()
    with os.popen('git log -1 --pretty=format:%ct') as f:
        VERSION_TIMESTAMP = datetime.datetime.fromtimestamp(int(f.readline().strip()), datetime.timezone.utc)
except:
#    print('Failed to read version info from git')
    pass

DEPLOYMENT_NAME = 'development'

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'django.template.context_processors.debug',
]

INSTALLED_APPS += (
   'debug_toolbar',
    'django_extensions',
    'django_nose'
)

LOGGING['loggers']['{{ project_name }}'] = {
    'handlers': ['console'],
    'level': 'DEBUG'
}

LOGGING['formatters']['verbose']['()'] = 'coloredlogs.ColoredFormatter'

# NOTE: the below enforces http authentication (will return a 401)
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework.authentication.BasicAuthentication',) + REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']

REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'

# Test settings
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--all-modules',
    '--with-yanc',
    '--verbosity=2'
]

# NOSE_PLUGINS = []

# Sent mail is saved in files (rather than actually being sent) in development mode
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tests/sent_mail'
# Optionally you can send email to the console (add the below line to local.py, don't edit this
# file)
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MINIFIED_JS = False

DEBUG_TOOLBAR_CONFIG = {
    # Provide our own local version here so that we can use the toolbar even when offline
    'JQUERY_URL': STATIC_URL + 'js/vendor/jquery-1.11.0.min.js',
    'SHOW_TEMPLATE_CONTEXT': True,

}

# Raven/Sentry -- please insert your raven config into local.py. Template below. Remember to append
#  verify_ssl=0 at the end as we don't have a RootCA signed certificate on the server yet.
#
#RAVEN_CONFIG = {
#    'dsn': 'https://..../?verify_ssl=0',
#}

ALLOWED_HOSTS = ['*']

#ADMIN_HEADER_BACKGROUND = 'linear-gradient(#307d0e, #2e680e)'
ADMIN_LABEL_BACKGROUND = '#307d0e'
ADMIN_LABEL_COLOR = 'white'

SITE_ID = 3
SITE_CONFIG = {
    'name': 'development',
    'domain': ''
}

CORS_ORIGIN_ALLOW_ALL = True

try:
    from .local import *
except ImportError:
    # local settings is not mandatory
    pass
