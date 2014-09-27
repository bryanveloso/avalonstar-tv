# -*- coding: utf-8 -*-
from django.db import models

from components.games.models import Game


class Series(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = u'series'

    def __unicode__(self):
        return u'%s' % self.name


class Broadcast(models.Model):
    # Metadata.
    number = models.IntegerField(blank=True, null=True)
    airdate = models.DateField()
    status = models.CharField(blank=True, max_length=200,
        help_text=u'Loosely related to Twitch\'s status field. Does not need to match. Will display on overlays.')
    notes = models.TextField(blank=True)

    # Connections.
    games = models.ManyToManyField(Game, related_name='appears_on')
    series = models.ForeignKey(Series, blank=True, null=True, related_name='broadcasts',
        help_text=u'Is this episode part of an ongoing series (i.e., "Whatever Wednesdays", etc.)?')

    # Statuses.
    is_charity = models.BooleanField('is for charity?', default=False,
        help_text=u'Is a charity fundraiser involved in this episode?')
    is_marathon = models.BooleanField('is a marathon?', default=False,
        help_text=u'Is this a marathon episode (longer than 12 hours)?')

    class Meta:
        get_latest_by = 'airdate'
        ordering = ['-number']

    def __unicode__(self):
        return u'Episode %s' % self.number
