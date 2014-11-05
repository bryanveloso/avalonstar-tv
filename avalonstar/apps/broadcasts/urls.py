# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import BroadcastDetailView, BroadcastListView


urlpatterns = patterns('',
    url(r'^episode/(?P<slug>[-\w]+)/$', name='episode-detail', view=BroadcastDetailView.as_view()),
    url(r'^broadcasts/$', name='broadcast-list', view=BroadcastListView.as_view()),
)
