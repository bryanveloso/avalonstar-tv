# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0013_auto_20150505_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='is_charity',
            field=models.BooleanField(verbose_name='is for charity?', help_text='Is a charity fundraiser involved in this episode?', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='is_marathon',
            field=models.BooleanField(verbose_name='is a marathon?', help_text='Is this a marathon episode (longer than 12 hours)?', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='highlight',
            name='twid',
            field=models.CharField(verbose_name='Twitch ID', help_text="The highlight's ID on Twitch; used for API calls, etc.", max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='highlight',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL'),
            preserve_default=True,
        ),
    ]
