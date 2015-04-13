# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import views, viewsets
from rest_framework.response import Response
from pusher import Pusher

from apps.broadcasts.models import Broadcast, Host, Raid, Series
from apps.games.models import Game
from apps.subscribers.models import Ticket

from .serializers import (BroadcastSerializer, GameSerializer, HostSerializer,
    RaidSerializer, SeriesSerializer, TicketSerializer)


def notify(event, data):
    pusher['live'].trigger(event, data)


class BroadcastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Broadcast.objects.order_by('-number')
    serializer_class = BroadcastSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.order_by('-timestamp')
    serializer_class = HostSerializer

    def create(self, request, *args, **kwargs):
        notify('hosted', {'username': request.data['username']})
        return super(HostViewSet, self).update(request, *args, **kwargs)


class RaidViewSet(viewsets.ModelViewSet):
    queryset = Raid.objects.order_by('-timestamp')
    serializer_class = RaidSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.order_by('-updated')
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        notify('subscribed', {'username': request.data['username']})
        return super(TicketViewSet, self).update(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, name=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # If 'length' is included in the payload, then we consider it a
        # "substreak" and should notify() as such.
        if 'length' in request.data:
            notify('substreaked', {
                'length': request.data['length'],
                'username': request.data['username']})
        else:
            notify('resubscribed', {'username': request.data['username']})
        return super(TicketViewSet, self).update(request, *args, **kwargs)


# Pusher.
pusher = Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET)


class PusherDonationView(views.APIView):
    pass


class PusherHostView(views.APIView):
    def post(self, request):
        notify('hosted', request.data)
        return Response(status=202)


class PusherResubscriptionView(views.APIView):
    def post(self, request):
        notify('resubscribed', request.data)
        return Response(status=202)


class PusherSubscriptionView(views.APIView):
    def post(self, request):
        notify('subscribed', request.data)
        return Response(status=202)


class PusherSubstreakView(views.APIView):
    def post(self, request):
        notify('substreaked', request.data)
        return Response(status=202)
