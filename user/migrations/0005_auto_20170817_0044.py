# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-17 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170813_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pictureUrl',
            field=models.URLField(default='http://127.0.0.1:8000/static/users_avaters/default.jpg'),
        ),
    ]
