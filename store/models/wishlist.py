from django.db import models
from .customer import Customer
from .product import Product
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    