# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PG(models.Model):
    pg_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    owner_phone = models.BigIntegerField(default=00000)
    pg_price = models.IntegerField(default=0)
    pg_descp = models.TextField(max_length=250)
    image = models.CharField(max_length=250)
    loc_area = models.CharField(max_length=50,default='')
    loc_street = models.CharField(max_length=50,default='')
    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)


    def __str__(self):
        return self.pg_name +'-'+ self.owner_name
