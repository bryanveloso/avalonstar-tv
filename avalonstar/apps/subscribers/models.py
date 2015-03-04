# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class CountManager(models.Manager):
    def create_count(self):
        total = Ticket.objects.count()
        count = Count(total=total, timestamp=timezone.now())
        count.save()
        return count

class Count(models.Model):
    total = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now())

    # Custom manager.
    objects = CountManager()

    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        return u'%s on %s' % (self.total, self.timestamp)


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
