# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0007_auto_20150309_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['updated']},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='subscribed',
            new_name='updated'
        ),
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 22, 9, 37, 300476, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
