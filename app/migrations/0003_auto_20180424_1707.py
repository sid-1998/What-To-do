# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180424_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
