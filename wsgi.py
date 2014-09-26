# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avalonstar.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
