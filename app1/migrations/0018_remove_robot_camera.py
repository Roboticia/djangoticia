# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-27 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_merge_20170127_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='camera',
        ),
    ]
