# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Count(models.Model):
    total = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return u'%s' % self.timestamp


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

    class Meta:
        ordering = ['subscribed']

    def __unicode__(self):
        return u'%s' % self.name
