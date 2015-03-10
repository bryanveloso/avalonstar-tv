# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

from rest_framework import routers

from .views import BroadcastViewSet, HostViewSet, RaidViewSet, TicketViewSet


router = routers.DefaultRouter()
router.register(r'broadcasts', BroadcastViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'raids', RaidViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
