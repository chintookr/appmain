# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170711_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('8a72f103-67f5-41d1-a67a-0a86ed043ce8'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
