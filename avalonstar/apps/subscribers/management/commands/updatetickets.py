# -*- coding: utf-8 -*-
import requests
import os

from django.core.management.base import NoArgsCommand, CommandError

from apps.subscribers.models import Ticket


class Command(NoArgsCommand):
    help = u'Loops through all subscribers and marks each ticket appropriately.'

    def handle_noargs(self, **options):
        # Rather than mark active tickets as inactive, mark all tickets as
        # inactive. As we loop through the Twitch API, we'll mark
        tickets = Ticket.objects.update(is_active=False)

        # Prepare our request.
        headers = {
            'Authorization': 'OAuth %s' % os.environ.get('TWITCH_OAUTH_TOKEN'),
            'Accept': 'application/vnd.twitchtv.v3+json' }
        url = 'https://api.twitch.tv/kraken/channels/avalonstar/subscriptions'
        r = requests.get(url, headers=headers)
        count = r.json()['_total']  # Total number of tickets.
        limit = 100  # Maximum number of tickets we can fetch at once.

        while url:
            response = requests.get(url, headers=headers, params={'limit': limit})
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
                t.is_active = True

                # Set some other things while we're here.
                t.display_name = ticket['user']['display_name']
                t.subscribed = ticket['created_at']
                t.twid = ticket['_id']

                # Save it all.
                t.save()

            # Done. Grab `next` and keep looping.
            url = data['_links']['next']
