# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_auto_20160926_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='cad',
            field=models.DecimalField(decimal_places=2, default=1.39, max_digits=19),
        ),
        migrations.AddField(
            model_name='currency',
            name='clp',
            field=models.DecimalField(decimal_places=2, default=2.56, max_digits=19),
        ),
        migrations.AddField(
            model_name='currency',
            name='cop',
            field=models.DecimalField(decimal_places=2, default=2.09, max_digits=19),
        ),
        migrations.AddField(
            model_name='currency',
            name='egp',
            field=models.DecimalField(decimal_places=2, default=3.39, max_digits=19),
        ),
    ]
