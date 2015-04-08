# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0011_auto_20150305_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='hoster',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='raid',
            old_name='raider',
            new_name='username',
        ),
    ]
