# -*- coding: utf-8 -*-
from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=200)
    subtext = models.CharField(max_length=200)

    class Meta:
        ordering = ['text']

    def __unicode__(self):
        return u'%s' % self.text
