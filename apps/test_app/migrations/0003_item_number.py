# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]