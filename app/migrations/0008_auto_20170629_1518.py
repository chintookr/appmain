# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170629_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='appreq',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('c969a934-14ad-4b21-aa45-663c8351b543'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
