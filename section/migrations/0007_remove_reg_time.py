# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-14 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0006_auto_20170514_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='time',
        ),
    ]
