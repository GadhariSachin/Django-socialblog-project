# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-02 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='new-article', max_length=128),
        ),
    ]