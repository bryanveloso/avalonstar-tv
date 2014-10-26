# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

from rest_framework import routers

from .views import BroadcastViewSet, RaidViewSet


router = routers.DefaultRouter()
router.register(r'broadcasts', BroadcastViewSet)
router.register(r'raids', RaidViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
