# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20170713_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('07eb83b7-8754-4c46-ac7e-efbabd67068e'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]