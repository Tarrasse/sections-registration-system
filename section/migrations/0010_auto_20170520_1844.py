# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-20 16:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0009_auto_20170520_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='Students',
            new_name='Students',
        ),
        migrations.RemoveField(
            model_name='section',
            name='available',
        ),
    ]
