# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-11 04:21
from __future__ import unicode_literals

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160811_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default=b'Australia/Perth'),
        ),
    ]
