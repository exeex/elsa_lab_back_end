# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-26 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20170820_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='studentType',
            field=models.CharField(choices=[('1', 'course_student'), ('2', 'College'), ('3', 'Master'), ('4', 'PHD'), ('5', 'Teacher'), ('6', 'Alumni')], max_length=1),
        ),
    ]
