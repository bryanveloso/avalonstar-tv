# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0010_auto_20150403_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='streak',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 4, 1, 5, 15, 793199, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
