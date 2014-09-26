# -*- coding: utf-8 -*-
from django.db import models

from components.games.models import Game


class Series(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.name


class Broadcast(models.Model):
    airdate = models.DateField()
    status = models.CharField(max_length=200)
    number = models.IntegerField(blank=True, null=True)

    # ...
    games = models.ManyToManyField(Game, related_name='appears_on')
    series = models.ForeignKey(Series, related_name='broadcasts')

    # ...
    def __unicode__(self):
        return 'Episode %s' % self.number
