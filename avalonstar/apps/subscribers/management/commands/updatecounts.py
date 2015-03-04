# -*- coding: utf-8 -*-
from django.core.management.base import NoArgsCommand

from apps.subscribers.models import Count


class Command(NoArgsCommand):
    help = u'Counts and saves the total number of subscriptions for the current day.'

    def handle_noargs(self, **options):
        count = Count.objects.create_count()
        return count
