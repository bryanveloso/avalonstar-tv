# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0004_auto_20150224_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 3, 4, 1, 52, 0, 594138, tzinfo=utc))),
            ],
            options={
                'ordering': ['timestamp'],
            },
            bases=(models.Model,),
        ),
    ]
