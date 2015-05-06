# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import views, viewsets
from rest_framework.response import Response
from socketIO_client import SocketIO

from apps.broadcasts.models import Broadcast, Host, Raid, Series
from apps.games.models import Game, Platform
from apps.quotes.models import Quote
from apps.subscribers.models import Ticket

from .serializers import (BroadcastSerializer, GameSerializer, HostSerializer,
    PlatformSerializer, QuoteSerializer, RaidSerializer, SeriesSerializer,
    TicketSerializer)


def notify(event, data):
    data = data.copy()
    data['event'] = event

    with SocketIO('socket.avalonstar.tv') as socketIO:
        socketIO.emit('event sent', data)
        socketIO.wait(seconds=1)


class BroadcastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Broadcast.objects.order_by('-number')
    serializer_class = BroadcastSerializer


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def retrieve(self, request, pk=None):
        if pk == '0':
            quote = Quote.objects.order_by('?').first()
            serializer = QuoteSerializer(quote)
            return Response(serializer.data)
        else:
            return super(QuoteViewSet, self).retrieve(request, pk)


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.order_by('-timestamp')
    serializer_class = HostSerializer

    def create(self, request, *args, **kwargs):
        notify('host', {'username': request.data['username']})
        return super(HostViewSet, self).create(request, *args, **kwargs)


class RaidViewSet(viewsets.ModelViewSet):
    queryset = Raid.objects.order_by('-timestamp')
    serializer_class = RaidSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.order_by('-updated')
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        # TODO: Somehow sync the use of "name" and "username" across methods.
        notify('subscription', {'username': request.data['name']})
        return super(TicketViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, name=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data.copy()
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, name=pk)

        data['name'] = ticket.name
        serializer = TicketSerializer(ticket, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # If 'streak' is included in the payload, then we consider it a
        # "substreak" and should notify() as such.
        if 'streak' in request.data:
            notify('substreak', {
                'length': data['streak'],
                'username': ticket.name})
        else:
            notify('resubscription', {'username': ticket.name})
        return Response(serializer.data)


class PusherDonationView(views.APIView):
    def post(self, request):
        notify('donation', request.data)
        return Response(status=202)


class PusherHostView(views.APIView):
    def post(self, request):
        notify('host', request.data)
        return Response(status=202)


class PusherResubscriptionView(views.APIView):
    def post(self, request):
        notify('resubscription', request.data)
        return Response(status=202)


class PusherSubscriptionView(views.APIView):
    def post(self, request):
        notify('subscription', request.data)
        return Response(status=202)


class PusherSubstreakView(views.APIView):
    def post(self, request):
        notify('substreak', request.data)
        return Response(status=202)
