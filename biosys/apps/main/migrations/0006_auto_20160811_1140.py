# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-11 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160805_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='observation_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='speciesobservation',
            old_name='observation_date',
            new_name='date',
        ),
    ]
