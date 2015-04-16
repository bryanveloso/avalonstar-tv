# -*- coding: utf-8 -*-
import pytest

from .factories import GameFactory, PlatformFactory
from ..models import Game, Platform

pytestmark = pytest.mark.django_db


def test_game_factory():
    factory = GameFactory()
    assert isinstance(factory, Game)


def test_platform_factory():
    factory = PlatformFactory()
    assert isinstance(factory, Platform)
