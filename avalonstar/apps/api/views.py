# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

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


class TicketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def retrieve(self, request, pk=None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, name=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
