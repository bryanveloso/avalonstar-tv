# -*- coding: utf-8 -*-
from rest_framework import viewsets

from components.broadcasts.models import Broadcast, Series
from components.games.models import Game

from .serializers import BroadcastSerializer, GameSerializer, SeriesSerializer


class BroadcastViewSet(viewsets.ModelViewSet):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
