# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.broadcasts.models import Broadcast, Host, Raid, Series
from apps.games.models import Game
from apps.subscribers.models import Ticket


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'timestamp', 'username', 'broadcast')
        model = Host


class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'timestamp', 'username', 'broadcast', 'game')
        model = Raid


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket


class BroadcastSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    raids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Broadcast
