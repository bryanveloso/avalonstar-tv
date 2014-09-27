# -*- coding: utf-8 -*-
from rest_framework import serializers

from components.broadcasts.models import Broadcast, Series
from components.games.models import Game


class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast


class SeriesSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Series


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
