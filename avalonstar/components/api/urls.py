# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

from .views import BroadcastList, BroadcastDetail


broadcast_urls = patterns('',
    url(r'^/(?P<number>\d+)$', name='broadcast-detail', view=BroadcastDetail.as_view()),
    url(r'^$', name='broadcast-list', view=BroadcastList.as_view()),
)

urlpatterns = patterns('',
    url(r'^broadcasts', include(broadcast_urls)),
)
