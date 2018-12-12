from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Shop(models.Model):
    item = models.CharField(max_length=255)
    price = models.FloatField()