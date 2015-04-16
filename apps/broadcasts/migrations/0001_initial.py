# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('airdate', models.DateField()),
                ('status', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True)),
                ('is_charity', models.BooleanField(default=False)),
                ('is_marathon', models.BooleanField(default=False)),
                ('games', models.ManyToManyField(related_name=b'appears_on', to='games.Game')),
            ],
            options={
                'ordering': ['-number'],
                'get_latest_by': 'airdate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'series',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='series',
            field=models.ForeignKey(related_name=b'broadcasts', to='broadcasts.Series'),
            preserve_default=True,
        ),
    ]
