# -*- coding: utf-8 -*-
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from configurations import Configuration, values
from postgresify import postgresify


class Base(Configuration):
    # Path configuration.
    # --------------------------------------------------------------------------
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    SITE_ROOT = dirname(DJANGO_ROOT)
    SITE_NAME = basename(DJANGO_ROOT)

    # Add our project to our pythonpath, this way we don't need to
    # type our project name in our dotted import paths:
    path.append(DJANGO_ROOT)

    # Installed Applications.
    # --------------------------------------------------------------------------
    DJANGO = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    COMPONENTS = [
        'components.broadcasts',
        'components.games',
    ]
    PLUGINS = []
    ADMINISTRATION = [
        'grappelli',
        'django.contrib.admin',
    ]
    INSTALLED_APPS = DJANGO + COMPONENTS + PLUGINS + ADMINISTRATION

    # Middleware Configuration.
    # --------------------------------------------------------------------------
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    # Debug Settings.
    # --------------------------------------------------------------------------
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    # Secret Key Configuration.
    # --------------------------------------------------------------------------
    SECRET_KEY = '+7wd8f!r%3@p)&%=td=63vi@d*i9_#2ln8ge+x&-4%$j$xrpo^'

    # Database Configuration.
    # --------------------------------------------------------------------------
    DATABASES = postgresify()

    # Internationalization.
    # --------------------------------------------------------------------------
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static File Configuration.
    # --------------------------------------------------------------------------
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    # Media Configuration.
    # --------------------------------------------------------------------------
    MEDIA_ROOT = 'media'
    MEDIA_URL = '/media/'

    # URL Configuration
    # --------------------------------------------------------------------------
    ROOT_URLCONF = '%s.urls' % SITE_NAME
    WSGI_APPLICATION = 'wsgi.application'

    # django-rest-framework.
    # --------------------------------------------------------------------------
    INSTALLED_APPS += ['rest_framework']
