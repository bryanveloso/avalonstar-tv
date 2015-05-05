# -*- coding: utf-8 -*-
import pytest

from .factories import QuoteFactory
from ..models import Quote

pytestmark = pytest.mark.django_db


def test_quote_factory():
    factory = QuoteFactory()
    assert isinstance(factory, Quote)
