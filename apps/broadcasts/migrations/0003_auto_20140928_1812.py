# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0002_auto_20140927_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='is_charity',
            field=models.BooleanField(default=False, help_text='Is a charity fundraiser involved in this episode?', verbose_name=b'is for charity?'),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='is_marathon',
            field=models.BooleanField(default=False, help_text='Is this a marathon episode (longer than 12 hours)?', verbose_name=b'is a marathon?'),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='series',
            field=models.ForeignKey(related_name=b'broadcasts', blank=True, to='broadcasts.Series', help_text='Is this episode part of an ongoing series (i.e., "Whatever Wednesdays", etc.)?', null=True),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='status',
            field=models.CharField(help_text="Loosely related to Twitch's status field. Does not need to match. Will display on overlays.", max_length=200, blank=True),
        ),
    ]
