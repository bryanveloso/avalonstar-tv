# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0011_auto_20150403_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 5, 20, 30, 926786, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
