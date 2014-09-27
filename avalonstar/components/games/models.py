# -*- coding: utf-8 -*-
from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name


class Game(models.Model):
    # Metadata.
    gbid = models.CharField('Giant Bomb ID', max_length=10)
    name = models.CharField(max_length=200)
    platform = models.ForeignKey(Platform, null=True, related_name='games')

    # Statuses.
    is_abandoned = models.BooleanField('is abandoned?', default=False)
    is_completed = models.BooleanField('is completed?', default=False)

    def __unicode__(self):
        return u'%s' % self.name
