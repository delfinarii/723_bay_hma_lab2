# -*- coding: utf-8 -*-
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=50)
    char = models.CharField(max_length=200)
    company = models.CharField(max_length=30)
    year = models.IntegerField()

    
class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    phone = models.CharField(max_length=17, blank=True)
    works = models.CharField(max_length=100, blank=True)


class Buy(models.Model):
    device = models.ForeignKey(Device)
    shop = models.ForeignKey(Shop)
    price = models.FloatField()
    emount = models.IntegerField()
