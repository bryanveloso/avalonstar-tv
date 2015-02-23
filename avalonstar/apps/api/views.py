# -*- coding: utf-8 -*-
from rest_framework import viewsets

from apps.broadcasts.models import Broadcast, Raid, Series
from apps.games.models import Game
from apps.subscribers.models import Ticket

from .serializers import (BroadcastSerializer, GameSerializer, RaidSerializer,
    SeriesSerializer, TicketSerializer)


class BroadcastViewSet(viewsets.ModelViewSet):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer


class RaidViewSet(viewsets.ModelViewSet):
    queryset = Raid.objects.all()
    serializer_class = RaidSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
