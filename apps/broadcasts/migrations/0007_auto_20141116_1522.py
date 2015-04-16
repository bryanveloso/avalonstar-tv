# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0006_auto_20141029_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='twid',
            field=models.CharField(default='', help_text="The highlight's ID on Twitch; used for API calls, etc.", max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='highlight',
            name='game',
            field=models.ForeignKey(related_name=b'highlited_on', blank=True, to='games.Game'),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='url',
            field=models.URLField(verbose_name=b'URL'),
        ),
    ]
