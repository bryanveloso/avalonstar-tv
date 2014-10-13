# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url

from .views import AwayView, BumperView, GameView, PrologueView


urlpatterns = patterns('',
    url(r'^away/$', name='live-away', view=AwayView.as_view()),
    url(r'^bumper/$', name='live-bumper', view=BumperView.as_view()),
    url(r'^game/$', name='live-game', view=GameView.as_view()),
    url(r'^prologue/$', name='live-prologue', view=PrologueView.as_view()),
)
