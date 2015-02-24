# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_auto_20150223_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='display_name',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subscribed',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='When did the user subscribe?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='twid',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
    ]
