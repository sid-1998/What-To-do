# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='text',
            field=models.CharField(help_text='ENTER TODO', max_length=100),
        ),
    ]
