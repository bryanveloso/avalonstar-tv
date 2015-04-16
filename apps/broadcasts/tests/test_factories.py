# -*- coding: utf-8 -*-
import pytest

from .factories import (BroadcastFactory, HighlightFactory,
    HostFactory, RaidFactory, SeriesFactory)
from ..models import Broadcast, Highlight, Host, Raid, Series

pytestmark = pytest.mark.django_db


def test_broadcast_factory():
    factory = BroadcastFactory()
    assert isinstance(factory, Broadcast)


def test_host_factory():
    factory = HostFactory()
    assert isinstance(factory, Host)


def test_raid_factory():
    factory = RaidFactory()
    assert isinstance(factory, Raid)


def test_series_factory():
    factory = SeriesFactory()
    assert isinstance(factory, Series)
