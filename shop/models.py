from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchase', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_delivered = models.BooleanField(default=False)
    pay_money = models.DateTimeField(auto_now_add=True)
    take_product = models.DateTimeField(null=True)

    def get_total(self):
        return self.quantity * self.product.price
