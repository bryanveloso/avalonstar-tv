# -*- coding: utf-8 -*-
from rest_framework import viewsets

from apps.broadcasts.models import Broadcast, Series
from apps.games.models import Game

from .serializers import BroadcastSerializer, GameSerializer, SeriesSerializer


class BroadcastViewSet(viewsets.ModelViewSet):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
