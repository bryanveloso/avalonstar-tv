# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0012_auto_20150407_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
