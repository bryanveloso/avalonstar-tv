# -*- coding: utf-8 -*-
import factory

from ..models import Quote


class QuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quote
