# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0008_auto_20150321_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 22, 21, 7, 920762, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
