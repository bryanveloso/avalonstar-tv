# -*- coding: utf-8 -*-
import requests
import os

from django.core.management.base import NoArgsCommand

from apps.subscribers.models import Ticket


class Command(NoArgsCommand):
    help = u'Loops through all subscribers and marks each ticket appropriately.'

    def handle_noargs(self, **options):
        # Rather than mark active tickets as inactive, mark all tickets as
        # inactive. As we loop through the Twitch API, we'll mark
        Ticket.objects.invalidate_tickets()

        # Prepare our request.
        headers = {
            'Authorization': 'OAuth %s' % os.environ.get('TWITCH_OAUTH_TOKEN'),
            'Accept': 'application/vnd.twitchtv.v3+json' }
        url = 'https://api.twitch.tv/kraken/channels/avalonstar/subscriptions'
        r = requests.get(url, headers=headers)
        count = r.json()['_total']  # Total number of tickets.
        limit = 100  # Maximum number of tickets we can fetch at once.

        while url:
            # To keep our dyno-hour usage down, we have to make sure that
            # requests aren't hung up. So try the request and if a `Timeout`
            # is thrown, bail.
            try:
                response = requests.get(url, headers=headers, params={'limit': limit}, timeout=1)
            except requests.exceptions.Timeout:
                break

            data = response.json()
            tickets = data['subscriptions']

            # The Twitch API doesn't stop offering `next` URLs when no results
            # are available. So if we don't have tickets, shut it down.
            if not tickets:
                break

            # We have tickets. Let's check each ticket and mark if that person
            # as active if their ticket still exists in Twitch's API.
            for ticket in tickets:
                name = ticket['user']['name']
                print name
                t = Ticket.objects.get(name=name)
                updates = {
                    'display_name': ticket['user']['display_name'],
                    'is_active': True,
                    'subscribed': ticket['created_at'],
                    'twid': ticket['_id'] }
                t.update(**updates)

            # Done. Grab `next` and keep looping.
            url = data['_links']['next']
