from .base_settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SENDGRID_SANDBOX_MODE_IN_DEBUG = DEBUG

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
}

AWS_ACCESS_KEY_ID = 'AKIAJUK4HNUS7WY7VQ6Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sdasgroup'
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'service.app.storage_backends.MediaStorage'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rtafarimakonnen@gmail.com'
EMAIL_HOST_PASSWORD = 'Remalleulli1094*'
EMAIL_PORT = 587
