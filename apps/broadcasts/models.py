# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.games.models import Game


class Series(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'series'

    def __str__(self):
        return u'%s' % self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('name__exact', 'name__icontains')


class Broadcast(models.Model):
    # Metadata.
    number = models.IntegerField(blank=True, null=True)
    airdate = models.DateField(default=timezone.now)
    status = models.CharField(blank=True, max_length=200,
        help_text='Loosely related to Twitch\'s status field. Does not need to match. Will display on overlays.')
    notes = models.TextField(blank=True)

    # Connections.
    games = models.ManyToManyField(Game, related_name='appears_on')
    series = models.ForeignKey(Series, blank=True, null=True, related_name='broadcasts',
        help_text='Is this episode part of an ongoing series (i.e., "Whatever Wednesdays", etc.)?')

    # Statuses.
    is_charity = models.BooleanField('is for charity?', default=False,
        help_text='Is a charity fundraiser involved in this episode?')
    is_marathon = models.BooleanField('is a marathon?', default=False,
        help_text='Is this a marathon episode (longer than 12 hours)?')

    class Meta:
        get_latest_by = 'airdate'
        ordering = ['-airdate']

    def __str__(self):
        return 'Episode %s' % self.number

    def get_absolute_url(self):
        return reverse('broadcast-detail', kwargs={'slug': self.number})


class Highlight(models.Model):
    broadcast = models.ForeignKey(Broadcast, blank=True, null=True, related_name='highlights')
    twid = models.CharField('Twitch ID', max_length=200,
        help_text='The highlight\'s ID on Twitch; used for API calls, etc.')

    # Silly metadata (filled out by an API call).
    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField('URL', blank=True)
    game = models.ForeignKey(Game, blank=True, null=True, related_name='highlited_on')

    class Meta:
        ordering = ['-twid']
        order_with_respect_to = 'broadcast'

    def save(self, *args, **kwargs):
        # Grab our new highlight ID and run an API call.
        import requests
        endpoint = 'https://api.twitch.tv/kraken/videos/%s' % self.twid
        json = requests.get(endpoint).json()

        # Take the response and save it to the instance.
        # But first, find the game, so we can save that.
        if json['game']:
            game = Game.objects.get(name=json['game'])
            self.game = game
        self.description = json['description']
        self.title = json['title']
        self.url = json['url']
        super(Highlight, self).save(*args, **kwargs)

    def __str__(self):
        if not self.title:
            return 'Highlight for %s' % self.broadcast
        return self.title


class Host(models.Model):
    broadcast = models.ForeignKey(Broadcast, related_name='hosts')
    timestamp = models.DateTimeField(default=timezone.now,
        help_text='When did it happen?')
    username = models.CharField(blank=True, max_length=200)

    class Meta:
        order_with_respect_to = 'broadcast'
        ordering = ['timestamp']

    def __str__(self):
        return u'%s' % self.username


class Raid(models.Model):
    broadcast = models.ForeignKey(Broadcast, related_name='raids')
    timestamp = models.DateTimeField(default=timezone.now,
        help_text='When did it happen?')
    username = models.CharField(blank=True, max_length=200)

    # Silly metadata.
    game = models.CharField(blank=True, max_length=200,
        help_text='The game the raider was playing at the time of raiding.')

    class Meta:
        order_with_respect_to = 'broadcast'
        ordering = ['timestamp']

    def __str__(self):
        return u'%s' % self.username
