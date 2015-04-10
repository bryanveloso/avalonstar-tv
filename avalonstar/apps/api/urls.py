# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

from rest_framework import routers

from .views import (BroadcastViewSet, HostViewSet, RaidViewSet, TicketViewSet,
    PusherHostView, PusherResubscriptionView, PusherSubscriptionView,
    PusherSubstreakView)


router = routers.DefaultRouter()
router.register(r'broadcasts', BroadcastViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'raids', RaidViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = patterns('',
    # Pusher.
    url(r'^pusher/host/$', name='pusher-host', view=PusherHostView.as_view()),
    url(r'^pusher/resubscription/$', name='pusher-resubscription', view=PusherResubscriptionView.as_view()),
    url(r'^pusher/subscription/$', name='pusher-subscription', view=PusherSubscriptionView.as_view()),
    url(r'^pusher/substreak/$', name='pusher-substreak', view=PusherSubstreakView.as_view()),

    url(r'^', include(router.urls)),
)
