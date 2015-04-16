# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0003_auto_20140928_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raider', models.CharField(max_length=200, blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, help_text='Entered as a weird ass UNIX timestamp for legacy Firebase reasons.')),
                ('broadcast', models.ForeignKey(related_name=b'raids', to='broadcasts.Broadcast')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterOrderWithRespectTo(
            name='raid',
            order_with_respect_to='broadcast',
        ),
        migrations.AlterModelOptions(
            name='broadcast',
            options={'ordering': ['-airdate'], 'get_latest_by': 'airdate'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['name'], 'verbose_name_plural': 'series'},
        ),
    ]
