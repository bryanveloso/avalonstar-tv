# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.broadcasts.models import Broadcast, Raid, Series
from apps.games.models import Game


class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Broadcast


class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
