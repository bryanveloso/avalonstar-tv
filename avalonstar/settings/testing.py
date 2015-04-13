# -*- coding: utf-8 -*-
from configurations import values

from .base import Base as Settings


class Testing(Settings):
    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = values.BooleanValue(False)

    # Database Configuration.
    # --------------------------------------------------------------------------
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

    # pusher.
    # --------------------------------------------------------------------------
    PUSHER_APP_ID = ''
    PUSHER_KEY = ''
    PUSHER_SECRET = ''
