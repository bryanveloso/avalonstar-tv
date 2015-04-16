# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
                ('subscribed', models.DateTimeField(help_text='When did the user subscribe?')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['subscribed'],
            },
            bases=(models.Model,),
        ),
    ]
