from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name_plural = 'products'