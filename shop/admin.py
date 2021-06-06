from django.contrib import admin
from .models import Product, Purchase


admin.site.register(Purchase)
admin.site.register(Product)


