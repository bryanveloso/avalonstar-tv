# -*- coding: utf-8 -*-
import factory

from ..models import Broadcast, Highlight, Host, Raid, Series


class SeriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Series


class BroadcastFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Broadcast


class HighlightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Highlight

    broadcast = factory.SubFactory(BroadcastFactory)
    twid = 'c4136304'


class HostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Host

    broadcast = factory.SubFactory(BroadcastFactory)


class RaidFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Raid

    broadcast = factory.SubFactory(BroadcastFactory)
