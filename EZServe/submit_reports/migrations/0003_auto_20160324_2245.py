# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit_reports', '0002_auto_20160324_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitreport',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='submitreport',
            name='start_time',
            field=models.TimeField(),
        ),
    ]