# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from avalonstar.apps.views import PlainTextView


urlpatterns = patterns('',
    # Core Modules.
    url(r'^api/', include('apps.api.urls', namespace='api')),
    url(r'^live/', include('apps.live.urls', namespace='live')),

    # Administration Modules.
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Sitemaps, Favicons, Robots, and Humans.
    url(r'^robots.txt$', name='robots', view=PlainTextView.as_view(template_name='robots.txt'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
