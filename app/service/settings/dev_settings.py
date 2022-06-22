from .base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SENDGRID_SANDBOX_MODE_IN_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda self: True
}

INSTALLED_APPS = [
    'django_extensions',
    'debug_toolbar',
] + INSTALLED_APPS


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
