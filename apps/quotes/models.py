# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from apps.broadcasts.models import Broadcast
from apps.games.models import Game


class Quote(models.Model):
    text = models.TextField()
    timestamp = models.DateField(default=timezone.now)
    broadcast = models.ForeignKey(Broadcast, blank=True, null=True, related_name='quotes')
    game = models.ForeignKey(Game, blank=True, null=True, related_name='quoted_on')

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return u'{}'.format(self.text)
