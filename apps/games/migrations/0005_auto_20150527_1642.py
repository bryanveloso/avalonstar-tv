# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20141025_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gbid',
            field=models.CharField(verbose_name='Giant Bomb ID', help_text='Usually in the form "3030-20678", etc.', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='image_art',
            field=models.ImageField(upload_to='games', blank=True, verbose_name='art', help_text='16:9 art. Used for backgrounds, etc. Minimum size should be 1280x720.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='image_boxart',
            field=models.ImageField(upload_to='games', blank=True, verbose_name='boxart', help_text='8:11 art akin to Twitch. Used for supplimentary display, lists, etc.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='is_abandoned',
            field=models.BooleanField(verbose_name='is abandoned?', help_text='Has this game been abandoned for good?', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='is_completed',
            field=models.BooleanField(verbose_name='is completed?', help_text='Has this game been completed (if applicable).', default=False),
            preserve_default=True,
        ),
    ]
