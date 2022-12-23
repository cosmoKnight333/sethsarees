from django.db import models
class Corousel(models.Model):
    name = models.CharField(max_length=50)
    heading = models.TextField( default='' , null=True , blank=True)
    subheading = models.TextField( default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    
    @staticmethod
    def get_all_corousels():
        return Corousel.objects.all()
        