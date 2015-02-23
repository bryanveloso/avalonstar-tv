# -*- coding: utf-8 -*-
from django.db import models


class Ticket(models.Model):
    twid = models.IntegerField()
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    subscribed = models.DateTimeField(help_text=u'When did the user subscribe?')

    # Is this subscription active?
    # TODO: Run a script that deactivates subs after XX days.
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['subscribed']

    def __unicode__(self):
        return u'%s' % self.name
