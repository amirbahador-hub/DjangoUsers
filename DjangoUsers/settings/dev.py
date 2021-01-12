from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

try:
    from DjangoUsers.settings.local import *
except Exception:
    pass

# INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")
