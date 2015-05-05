# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0013_auto_20150505_1510'),
        ('games', '0004_auto_20141025_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('broadcast', models.ForeignKey(related_name='quotes', blank=True, to='broadcasts.Broadcast', null=True)),
                ('game', models.ForeignKey(related_name='quoted_on', blank=True, to='games.Game', null=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
