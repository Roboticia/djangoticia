# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 12:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_robot_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='test',
        ),
    ]
