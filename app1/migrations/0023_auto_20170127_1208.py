# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-27 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_remove_info_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daemon',
            name='simulator',
        ),
        migrations.AlterField(
            model_name='robot',
            name='simulated',
            field=models.CharField(choices=[('Vrep', 'Vrep'), ('Poppy-simu', 'Poppy-simu'), ('Real robot', 'Real robot')], default='Real robot', max_length=1),
        ),
    ]