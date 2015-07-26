# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import BroadcastDetailView, BroadcastListView


urlpatterns = [
    url(r'^episode/(?P<slug>[-\w]+)/$', name='broadcast-detail', view=BroadcastDetailView.as_view()),
    url(r'^broadcasts/$', name='broadcast-list', view=BroadcastListView.as_view()),
]
