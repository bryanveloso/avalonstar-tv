# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20141025_2339'),
        ('broadcasts', '0005_raid_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200, blank=True)),
                ('description', models.TextField(blank=True)),
                ('broadcast', models.ForeignKey(related_name=b'highlights', to='broadcasts.Broadcast')),
                ('game', models.ForeignKey(related_name=b'highlited_on', to='games.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterOrderWithRespectTo(
            name='highlight',
            order_with_respect_to='broadcast',
        ),
        migrations.AlterField(
            model_name='raid',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='When did it happen?'),
        ),
    ]
