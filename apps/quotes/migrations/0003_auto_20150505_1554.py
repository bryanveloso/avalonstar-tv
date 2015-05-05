# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quote_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='subject',
            field=models.CharField(help_text='The person that was quoted.', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='creator',
            field=models.CharField(help_text='The person that created the quote.', max_length=200, blank=True),
        ),
    ]
