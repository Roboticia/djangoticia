# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20161006_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='host',
        ),
    ]
