# Generated by Django 2.0 on 2018-09-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180424_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='report',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
    ]
