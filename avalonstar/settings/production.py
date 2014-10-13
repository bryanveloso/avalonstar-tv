# -*- coding: utf-8 -*-
import os
import sys

from configurations import values
from postgresify import postgresify

from .base import Base as Settings


class Production(Settings):
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

    # Database Configuration.
    # --------------------------------------------------------------------------
    DATABASES = postgresify()
    if 'default' in DATABASES:  # pragma: no branch
        DATABASES['default']['CONN_MAX_AGE'] = 600
