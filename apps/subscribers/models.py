# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class CountManager(models.Manager):
    def create_count(self):
        total = Ticket.objects.count()
        active = Ticket.objects.filter(is_active=True, is_paid=True).count()
        if active is 0:
            active = Count.objects.exclude(active=0).latest()
        count = Count(active=active, total=total, timestamp=timezone.now())
        count.save()
        return count


class Count(models.Model):
    active = models.IntegerField()
    total = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    # Custom manager.
    objects = CountManager()

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['timestamp']

    def __str__(self):
        return '{}/{} on {}'.format(self.active, self.total, self.timestamp)


class TicketManager(models.Manager):
    def invalidate_tickets(self):
        self.update(is_active=False)


class Ticket(models.Model):
    twid = models.CharField(blank=True, max_length=40)
    name = models.CharField(max_length=200)
    display_name = models.CharField(blank=True, max_length=200)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    # Store the months if there's a substreak (defaults to 1 month).
    streak = models.IntegerField(default=1)

    # Is this subscription active?
    is_active = models.BooleanField(default=True,
        help_text='Is this subscription active?')
    is_paid = models.BooleanField(default=True,
        help_text='Is this a paid subscription? (e.g., Not a bot.)')

    # Custom manager.
    objects = TicketManager()

    class Meta:
        ordering = ['updated']
        get_latest_by = 'updated'

    def __str__(self):
        return '{}'.format(self.name)

    def update(self, **kwargs):
        allowed_attributes = {'twid', 'display_name', 'updated', 'is_active'}
        for name, value in kwargs.items():
            assert name in allowed_attributes
            setattr(self, name, value)
        self.save()
