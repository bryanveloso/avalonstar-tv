# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from apps.games.models import Game


class Series(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name_plural = u'series'

    def __unicode__(self):
        return u'%s' % self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('name__exact', 'name__icontains')


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
        ordering = ['-airdate']

    def __unicode__(self):
        return u'Episode %s' % self.number


class Highlight(models.Model):
    broadcast = models.ForeignKey(Broadcast, related_name='highlights')
    game = models.ForeignKey(Game, related_name='highlited_on')

    url = models.URLField()
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        order_with_respect_to = 'broadcast'

    def __unicode__(self):
        if not self.title:
            return u'Highlight for %s' % self.broadcast
        return self.title


class Raid(models.Model):
    broadcast = models.ForeignKey(Broadcast, related_name='raids')
    timestamp = models.DateTimeField(default=timezone.now,
        help_text=u'When did it happen?')
    raider = models.CharField(blank=True, max_length=200)

    # Silly metadata.
    game = models.CharField(blank=True, max_length=200,
        help_text=u'The game the raider was playing at the time of raiding.')

    class Meta:
        order_with_respect_to = u'broadcast'

    def __unicode__(self):
        return u'%s' % self.raider
