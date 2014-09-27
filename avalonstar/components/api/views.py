# -*- coding: utf-8 -*-
from rest_framework import generics

from components.broadcasts.models import Broadcast, Series
from components.games.models import Game

from .serializers import BroadcastSerializer, GameSerializer, SeriesSerializer


class BroadcastList(generics.ListAPIView):
    model = Broadcast
    serializer_class = BroadcastSerializer


class BroadcastDetail(generics.RetrieveAPIView):
    model = Broadcast
    lookup_field = 'number'
    serializer_class = BroadcastSerializer
