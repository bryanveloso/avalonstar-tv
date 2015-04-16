# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0008_auto_20141116_1933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='highlight',
            options={'ordering': ['-twid']},
        ),
        migrations.AlterField(
            model_name='highlight',
            name='broadcast',
            field=models.ForeignKey(related_name=b'highlights', blank=True, to='broadcasts.Broadcast', null=True),
        ),
    ]
