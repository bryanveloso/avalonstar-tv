# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0007_auto_20141116_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='highlight',
            options={'ordering': ['twid']},
        ),
        migrations.AlterField(
            model_name='highlight',
            name='game',
            field=models.ForeignKey(related_name=b'highlited_on', blank=True, to='games.Game', null=True),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='twid',
            field=models.CharField(help_text="The highlight's ID on Twitch; used for API calls, etc.", max_length=200, verbose_name=b'Twitch ID'),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='url',
            field=models.URLField(verbose_name=b'URL', blank=True),
        ),
    ]
