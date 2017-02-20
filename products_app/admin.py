from django.contrib import admin
from products_app import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Product, ProductAdmin)