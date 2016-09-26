# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_auto_20160926_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='aed',
            field=models.DecimalField(decimal_places=2, default=3.76, max_digits=19),
        ),
        migrations.AlterField(
            model_name='currency',
            name='bnd',
            field=models.DecimalField(decimal_places=2, default=1.41, max_digits=19),
        ),
        migrations.AlterField(
            model_name='currency',
            name='brl',
            field=models.DecimalField(decimal_places=2, default=3.98, max_digits=19),
        ),
    ]
