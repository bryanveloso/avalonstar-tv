# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(related_name=b'games', to='games.Platform', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='gbid',
            field=models.CharField(max_length=10, verbose_name=b'Giant Bomb ID'),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_abandoned',
            field=models.BooleanField(default=False, verbose_name=b'is abandoned?'),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name=b'is completed?'),
        ),
    ]
