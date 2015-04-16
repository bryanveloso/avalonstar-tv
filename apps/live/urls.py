# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from .views import (AwayView, DiscussionView, EpilogueView, GameView,
    NotifierView, PrologueView, StatusView)


urlpatterns = patterns('',
    # Because sooner or later, avalonstar.tv/ will be a welcome page.
    url(r'^$', name='site-home', view=RedirectView.as_view(url='http://twitch.tv/avalonstar')),

    # Overlays.
    url(r'^away/$', name='live-away', view=AwayView.as_view()),
    url(r'^discussion/$', name='live-discussion', view=DiscussionView.as_view()),
    url(r'^epilogue/$', name='live-epilogue', view=EpilogueView.as_view()),
    url(r'^game/$', name='live-game', view=GameView.as_view()),
    url(r'^prologue/$', name='live-prologue', view=PrologueView.as_view()),
    url(r'^notifier/$', name='live-notifier', view=NotifierView.as_view()),

    # Status (for bots).
    url(r'^status/$', name='live-status', view=StatusView.as_view()),
)