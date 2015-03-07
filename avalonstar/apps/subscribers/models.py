# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class CountManager(models.Manager):
    def create_count(self):
        active = Ticket.objects.filter(is_active=True, is_paid=True).count()
        total = Ticket.objects.count()
        count = Count(active=active, total=total, timestamp=timezone.now())
        count.save()
        return count


class Count(models.Model):
    active = models.IntegerField()
    total = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now())

    # Custom manager.
    objects = CountManager()

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['timestamp']

    def __unicode__(self):
        return u'%s/%s on %s' % (self.active, self.total, self.timestamp)


class TicketManager(models.Manager):
    def invalidate_tickets(self):
        self.update(is_active=False)


class Ticket(models.Model):
    twid = models.CharField(blank=True, max_length=40)
    name = models.CharField(max_length=200)
    display_name = models.CharField(blank=True, max_length=200)
    subscribed = models.DateTimeField(default=timezone.now,
        help_text=u'When did the user subscribe?')

    # Is this subscription active?
    # TODO: Run a script that deactivates subs after XX days.
    is_active = models.BooleanField(default=True,
        help_text=u'Is this subscription active?')
    is_paid = models.BooleanField(default=True,
        help_text=u'Is this a paid subscription? (e.g., Not a bot.)')

    # Custom manager.
    objects = TicketManager()

    class Meta:
        ordering = ['subscribed']

    def __unicode__(self):
        return u'%s' % self.name

    def update(self, **kwargs):
        allowed_attributes = {'twid', 'display_name', 'subscribed', 'is_active'}
        for name, value in kwargs.items():
            assert name in allowed_attributes
            setattr(self, name, value)
        self.save()
