# -*- coding: utf-8 -*-
from django.db import models


class Game(models.Model):
    gbid = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    # Statuses.
    is_abandoned = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.name
