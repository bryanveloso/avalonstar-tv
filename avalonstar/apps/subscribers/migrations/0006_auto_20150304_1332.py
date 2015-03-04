# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0005_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='active',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 4, 21, 32, 30, 445554, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
