# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-20 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0008_auto_20170520_1810'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Student',
        ),
    ]
