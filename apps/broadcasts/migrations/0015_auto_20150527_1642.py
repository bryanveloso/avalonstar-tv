# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0014_auto_20150527_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='broadcast',
            field=models.ForeignKey(null=True, to='broadcasts.Broadcast', related_name='hosts', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='raid',
            name='broadcast',
            field=models.ForeignKey(null=True, to='broadcasts.Broadcast', related_name='raids', blank=True),
            preserve_default=True,
        ),
    ]
