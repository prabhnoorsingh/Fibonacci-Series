# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0007_auto_20160913_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciseries',
            name='computation_time',
            field=models.FloatField(),
        ),
    ]
