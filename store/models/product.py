from django.db import models
from .category import Category
import random

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField( default='' , null=True , blank=True)
    short_description= models.TextField( default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    image1 = models.ImageField(upload_to='uploads/products/')
    image2 = models.ImageField(upload_to='uploads/products/')
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_product_by_id(id):
        return Product.objects.get(id=id)
        

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid_random(category_id):
        if category_id:
            items=Product.objects.filter(category=category_id)
            return random.sample(list(items), min(10,len(items)))
        else:
            Product.objects.all()

    def __str__(self):
        return self.name 