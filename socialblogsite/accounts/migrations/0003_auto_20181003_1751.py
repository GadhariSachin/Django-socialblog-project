# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-03 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181002_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default=b'default.jpeg', null=True, upload_to=b''),
        ),
    ]
