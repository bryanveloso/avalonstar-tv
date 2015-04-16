# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20140927_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image_art',
            field=models.ImageField(default='', upload_to=b'game', blank=True, help_text='16:9 art. Used for backgrounds, etc. Minimum size should be 1280x720.', verbose_name=b'art'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='image_boxart',
            field=models.ImageField(default='', upload_to=b'game', blank=True, help_text='8:11 art akin to Twitch. Used for supplimentary display, lists, etc.', verbose_name=b'boxart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='gbid',
            field=models.CharField(help_text='Usually in the form "3030-20678", etc.', max_length=10, verbose_name=b'Giant Bomb ID'),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_abandoned',
            field=models.BooleanField(default=False, help_text='Has this game been abandoned for good?', verbose_name=b'is abandoned?'),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_completed',
            field=models.BooleanField(default=False, help_text='Has this game been completed (if applicable).', verbose_name=b'is completed?'),
        ),
    ]
