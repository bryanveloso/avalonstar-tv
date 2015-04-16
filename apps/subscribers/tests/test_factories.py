# -*- coding: utf-8 -*-
import pytest

from .factories import TicketFactory
from ..models import Ticket

pytestmark = pytest.mark.django_db


def test_ticket_factory():
    factory = TicketFactory()
    assert isinstance(factory, Ticket)
