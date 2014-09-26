# -*- coding: utf-8 -*-
from django.db import models

from components.games.models import Game


class Series(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.name


class Broadcast(models.Model):
    number = models.IntegerField(blank=True, null=True)
    airdate = models.DateField()
    status = models.CharField(max_length=200)
    notes = models.TextField(blank=True)

    # Connections.
    games = models.ManyToManyField(Game, related_name='appears_on')
    series = models.ForeignKey(Series, related_name='broadcasts')

    # Statuses.
    is_charity = models.BooleanField(default=False)
    is_marathon = models.BooleanField(default=False)

    class Meta:
        get_latest_by = 'airdate'
        ordering = ['-number']

    def __unicode__(self):
        return 'Episode %s' % self.number
