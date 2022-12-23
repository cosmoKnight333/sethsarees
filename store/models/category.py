from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='uploads/category_img/')
    description = models.TextField( default='' , null=True , blank=True)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name 
    