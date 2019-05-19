#!/usr/bin/env python
# coding=utf-8

from .deployment import *

# NOTE: ideally this file is (mostly) empty as we want the staging environment to be as close
#  to the production as possible.

DEPLOYMENT_NAME = 'staging'

ALLOWED_HOSTS = []

SITE_ID = 2
SITE_CONFIG = {
    'name': 'staging',
    'domain': ''
}
