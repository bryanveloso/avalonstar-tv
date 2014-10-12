# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='series',
            field=models.ForeignKey(related_name=b'broadcasts', blank=True, to='broadcasts.Series', null=True),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='status',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
