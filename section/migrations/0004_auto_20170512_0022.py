# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-11 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_remove_client_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='data',
            new_name='date',
        ),
    ]