# -*- coding: utf-8 -*-
from rest_framework import viewsets

from apps.broadcasts.models import Broadcast, Raid, Series
from apps.games.models import Game

from .serializers import (BroadcastSerializer, GameSerializer, RaidSerializer,
    SeriesSerializer)


class BroadcastViewSet(viewsets.ModelViewSet):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer


class RaidViewSet(viewsets.ModelViewSet):
    queryset = Raid.objects.all()
    serializer_class = RaidSerializer
