#!/usr/bin/env python
# coding=utf-8

from .deployment import *

# NOTE: ideally this file is (mostly) empty as we want the staging environment to be as close
#  to the production as possible.

DEPLOYMENT_NAME = 'staging'

ALLOWED_HOSTS = []

ADMIN_HEADER_BACKGROUND = 'linear-gradient(#bebc30, #7d7b25)'
ADMIN_LABEL_BACKGROUND = 'yellow'
ADMIN_LABEL_COLOR = 'black'

SITE_ID = 2
SITE_CONFIG = {
    'name': 'staging',
    'domain': ''
}
