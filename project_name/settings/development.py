"""
Development settings.
"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INSTALLED_APPS += ('debug_toolbar',)

try:
    from .local import *
except ImportError:
    # local settings is not mandatory
    pass
