# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20150223_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_paid',
            field=models.BooleanField(default=True, help_text='Is this a paid subscription? (e.g., Not a bot.)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Is this subscription active?'),
            preserve_default=True,
        ),
    ]
