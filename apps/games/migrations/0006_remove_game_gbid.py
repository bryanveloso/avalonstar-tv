# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20150527_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gbid',
        ),
    ]
