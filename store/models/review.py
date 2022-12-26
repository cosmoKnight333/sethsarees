from django.db import models
class Review(models.Model):
    name = models.CharField(max_length=50)
    reviewer_name=models.CharField(max_length=50)
    description = models.TextField( default='' , null=True , blank=True)
    back_link= models.TextField( default='' , null=True , blank=True)
    @staticmethod
    def get_all_reviews():
        return Review.objects.all()
        