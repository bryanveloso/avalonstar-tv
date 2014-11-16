# -*- coding: utf-8 -*-
from configurations import values

from .base import Base as Settings


class Development(Settings):
    MIDDLEWARE_CLASSES = Settings.MIDDLEWARE_CLASSES

    # Site Configuration.
    # --------------------------------------------------------------------------
    ALLOWED_HOSTS = ['*']

    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(True)

    # Static File Configuration.
    # --------------------------------------------------------------------------
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Media Storage Configuration.
    # --------------------------------------------------------------------------
    CDN_DOMAIN = 'http://avalonstar-tv.s3.amazonaws.com'
    MEDIA_URL = '%s/' % (CDN_DOMAIN)
    STATIC_URL = '%s/static/' % (CDN_DOMAIN)
