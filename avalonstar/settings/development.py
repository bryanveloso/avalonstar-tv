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

    # django-staticbuilder.
    # --------------------------------------------------------------------------
    MIDDLEWARE_CLASSES += ('staticbuilder.middleware.BuildOnRequest',)
