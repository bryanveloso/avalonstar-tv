# -*- coding: utf-8 -*-
import factory

from ..models import Game, Platform


class PlatformFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Platform


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    platform = factory.SubFactory(PlatformFactory)
