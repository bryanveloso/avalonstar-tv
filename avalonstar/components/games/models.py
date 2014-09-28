# -*- coding: utf-8 -*-
from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name


class Game(models.Model):
    # Metadata.
    gbid = models.CharField('Giant Bomb ID', max_length=10,
        help_text=u'Usually in the form "3030-20678", etc.')
    name = models.CharField(max_length=200)
    platform = models.ForeignKey(Platform, null=True, related_name='games')

    # Imagery.
    image_art = models.ImageField('art', blank=True, upload_to='game',
        help_text=u'16:9 art. Used for backgrounds, etc. Minimum size should be 1280x720.')
    image_boxart = models.ImageField('boxart', blank=True, upload_to='game',
        help_text=u'8:11 art akin to Twitch. Used for supplimentary display, lists, etc.')

    # Statuses.
    is_abandoned = models.BooleanField('is abandoned?', default=False,
        help_text=u'Has this game been abandoned for good?')
    is_completed = models.BooleanField('is completed?', default=False,
        help_text=u'Has this game been completed (if applicable).' )

    def __unicode__(self):
        return u'%s' % self.name
