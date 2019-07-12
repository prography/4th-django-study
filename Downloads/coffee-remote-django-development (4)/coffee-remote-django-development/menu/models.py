from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    category = models.CharField(max_length=100, blank=True, default='')
