# -*- coding: utf-8 -*-
import os
import sys

from configurations import values
from postgresify import postgresify

from .base import Base as Settings


class Production(Settings):
    # Installed Applications (featuring Production).
    # --------------------------------------------------------------------------
    INSTALLED_APPS = Settings.INSTALLED_APPS + [
        'raven.contrib.django',
    ]

    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(False)

    # Secret Key Configuration.
    # --------------------------------------------------------------------------
    SECRET_KEY = os.environ.get('SECURE_KEY', '').split(',')[0]

    # Site Configuration.
    # --------------------------------------------------------------------------
    ALLOWED_HOSTS = [
        '.avalonstar.tv', '.avalonstar.tv.',
        '.avalonstar-tv.herokuapp.com', '.avalonstar-tv.herokuapp.com.',
    ]

    # Media Storage Configuration.
    # --------------------------------------------------------------------------
    INSTALLED_APPS += ['storages']
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # Amazon Web Services.
    AWS_ACCESS_KEY_ID = values.SecretValue(environ_prefix='')
    AWS_SECRET_ACCESS_KEY = values.SecretValue(environ_prefix='')
    AWS_STORAGE_BUCKET_NAME = values.SecretValue(environ_prefix='')
    AWS_AUTO_CREATE_BUCKET = True
    AWS_PRELOAD_METADATA = True
    AWS_QUERYSTRING_AUTH = False
    AWS_IS_GZIPPED = False

    # AWS Caching Settings.
    AWS_EXPIRY = 60 * 60 * 24 * 7
    AWS_HEADERS = {'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIRY, AWS_EXPIRY)}

    # ...
    CDN_DOMAIN = 'http://avalonstar-tv.s3.amazonaws.com'
    MEDIA_URL = '%s/' % (CDN_DOMAIN)

    # Database Configuration.
    # --------------------------------------------------------------------------
    DATABASES = postgresify()
    if 'default' in DATABASES:  # pragma: no branch
        DATABASES['default']['CONN_MAX_AGE'] = 600

    # Logging Configuration.
    # --------------------------------------------------------------------------
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
                'datefmt': '%d/%b/%Y %H:%M:%S'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'stream': sys.stdout
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.handlers.SentryHandler',
                'filters': ['require_debug_false'],
            },
        },
        'loggers': {
            # This is a "catch all" logger.
            '': {
                'level': 'DEBUG',
                'handlers': ['console', 'sentry'],
                'propagate': False,
            },
            'boto': {
                'level': 'WARNING',
                'handlers': ['sentry'],
                'propagate': False,
            },
        }
    }
