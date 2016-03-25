# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.broadcasts.models import Broadcast, Host, Raid, Series
from apps.games.models import Game, Platform
from apps.quotes.models import Quote
from apps.subscribers.models import Ticket


class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        import datetime
        return datetime.datetime.fromtimestamp(int(value))


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
    appearances = serializers.IntegerField(source='appears_on.count', read_only=True)

    class Meta:
        model = Game


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote


class TicketSerializer(serializers.ModelSerializer):
    created_at = UnixEpochDateField(source='created')
    updated_at = UnixEpochDateField(source='updated')

    class Meta:
        model = Ticket


class BroadcastSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    raids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Broadcast
