"""
Settings for {{ project_name }}

Settings for different environments are stored in separate files (modules).

.base (base.py) is always loaded first then the setting for the selected environment is
loaded. Environment specific settings can thus reference the values from .base

Environment selection is done in .environment.ENVIRONMENT (environment.py).
"""

import __builtin__
from .base import *
from . import environment

# NOTE: we might want to move the below logic to development env to avoid any
#  surprises in deployment.
env_name = os.environ.get('DJANGO_RUNTIME_ENVIRONMENT', environment.ENVIRONMENT)

__imported_module = __builtin__.__import__('%s' % env_name, globals(), locals(), ['*'], -1)
locals().update(__imported_module.__dict__)
