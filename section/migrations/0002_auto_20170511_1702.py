# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-11 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.IntegerField(),
        ),
    ]
