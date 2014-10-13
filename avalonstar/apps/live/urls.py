# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url

from .views import AwayView, BumperView


urlpatterns = patterns('',
    url(r'^/away/$', name='live-away', view=AwayView.as_view()),
    url(r'^/bumper/$', name='live-bumper', view=BumperView.as_view()),
)
