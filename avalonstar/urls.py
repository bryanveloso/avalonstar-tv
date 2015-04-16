# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

from apps.views import PlainTextView


urlpatterns = patterns('',
    # Temporary redirect to Twitch channel.
    url(r'^$', name='site-home', view=RedirectView.as_view(url='http://twitch.tv/avalonstar', permanent=False)),

    # Core Modules.
    url(r'^', include('apps.broadcasts.urls')),
    url(r'^', include('apps.games.urls')),
    url(r'^api/', include('apps.api.urls', namespace='api')),
    url(r'^live/', include('apps.live.urls', namespace='live')),

    # Administration Modules.
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Sitemaps, Favicons, Robots, and Humans.
    url(r'^favicon.ico$', name='favicon', view=RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),
    url(r'^robots.txt$', name='robots', view=PlainTextView.as_view(template_name='robots.txt'))
)
