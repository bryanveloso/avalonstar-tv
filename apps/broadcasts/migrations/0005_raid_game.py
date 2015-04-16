# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0004_auto_20141025_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='raid',
            name='game',
            field=models.CharField(default='', help_text='The game the raider was playing at the time of raiding.', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
