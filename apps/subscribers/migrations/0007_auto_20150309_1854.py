# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0006_auto_20150304_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='count',
            options={'ordering': ['timestamp'], 'get_latest_by': 'timestamp'},
        ),
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 1, 54, 17, 856, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
