from django.db import models
class BanarasPhoto(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/products/')
    
    @staticmethod
    def get_all_banaras_photos():
        return BanarasPhoto.objects.all()
        