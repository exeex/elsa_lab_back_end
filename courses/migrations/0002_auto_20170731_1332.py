# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='lecture_id',
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_number',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
