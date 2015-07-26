# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.views.generic import RedirectView

from .views import StatusView


urlpatterns = [
    # Because sooner or later, avalonstar.tv/ will be a welcome page.
    url(r'^$', name='site-home', view=RedirectView.as_view(url='http://twitch.tv/avalonstar', permanent=False)),

    # Status (for bots).
    url(r'^status/$', name='live-status', view=StatusView.as_view()),
]
