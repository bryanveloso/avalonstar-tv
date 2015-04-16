# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0010_auto_20150224_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, help_text='When did it happen?')),
                ('hoster', models.CharField(max_length=200, blank=True)),
                ('broadcast', models.ForeignKey(related_name='hosts', to='broadcasts.Broadcast')),
            ],
            options={
                'ordering': ['timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterOrderWithRespectTo(
            name='host',
            order_with_respect_to='broadcast',
        ),
    ]
