# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20170713_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('ace5fcb3-05e3-48da-97cd-4f3ba8f6b1aa'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='appreq',
            name='ename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.User'),
        ),
    ]