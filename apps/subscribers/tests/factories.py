# -*- coding: utf-8 -*-
import factory

from ..models import Ticket


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket
