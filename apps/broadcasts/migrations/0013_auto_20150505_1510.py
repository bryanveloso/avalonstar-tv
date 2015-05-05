# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0012_auto_20150407_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='airdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
