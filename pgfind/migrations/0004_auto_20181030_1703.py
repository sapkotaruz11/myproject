# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgfind', '0003_auto_20181030_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='pg',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='pg',
            name='image',
            field=models.CharField(max_length=1000),
        ),
    ]
