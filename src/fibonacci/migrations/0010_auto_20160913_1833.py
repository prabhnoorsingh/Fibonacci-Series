# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0009_auto_20160913_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciseries',
            name='nterms',
            field=models.IntegerField(),
        ),
    ]
