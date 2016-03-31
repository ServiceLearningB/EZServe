# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('summary', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
