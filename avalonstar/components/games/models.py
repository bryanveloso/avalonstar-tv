# -*- coding: utf-8 -*-
from django.db import models


class Game(models.Model):
    gbid = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % self.name
