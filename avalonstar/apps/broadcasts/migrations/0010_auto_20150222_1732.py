# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0009_auto_20141116_2230'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='raid',
            unique_together=set([('broadcast', 'raider')]),
        ),
    ]
