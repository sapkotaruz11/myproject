# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg_name', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_phone', models.BigIntegerField(default=0)),
                ('pg_price', models.IntegerField(default=0)),
                ('pg_descp', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='media/images/')),
            ],
        ),
    ]