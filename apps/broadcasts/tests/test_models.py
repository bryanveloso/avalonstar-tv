# -*- coding: utf-8 -*-
import pytest

from .factories import (BroadcastFactory)
from ..models import Broadcast

pytestmark = pytest.mark.django_db


class TestBroadcasts:
    def test_factory(self):
        factory = BroadcastFactory()
        assert isinstance(factory, Broadcast)
