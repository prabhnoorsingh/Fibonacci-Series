# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0003_auto_20160911_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciseries',
            name='value',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]