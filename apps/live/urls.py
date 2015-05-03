# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from .views import (AwayView, DiscussionView, EpilogueView, GameView,
    NotifierView, PrologueView, StatusView)


urlpatterns = patterns('',
    # Because sooner or later, avalonstar.tv/ will be a welcome page.
    url(r'^$', name='site-home', view=RedirectView.as_view(url='http://twitch.tv/avalonstar')),

    # Status (for bots).
    url(r'^status/$', name='live-status', view=StatusView.as_view()),
)
