# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='aed',
            field=models.DecimalField(decimal_places=10, default=1.22, max_digits=19),
        ),
    ]
