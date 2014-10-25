# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20140928_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='platform',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='game',
            name='image_art',
            field=models.ImageField(help_text='16:9 art. Used for backgrounds, etc. Minimum size should be 1280x720.', upload_to=b'games', verbose_name=b'art', blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='image_boxart',
            field=models.ImageField(help_text='8:11 art akin to Twitch. Used for supplimentary display, lists, etc.', upload_to=b'games', verbose_name=b'boxart', blank=True),
        ),
    ]
