# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20170711_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('ecbadc17-4029-4e8c-9f68-a9b32f34c23f'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]