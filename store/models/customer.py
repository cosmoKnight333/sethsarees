from django.db import models
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    phone_number=models.CharField(max_length=15)
    country_code=models.CharField(default='91' , null=True,max_length=15)
    verification_token=models.CharField(default='' , null=True,max_length=100)
    
    email=models.EmailField()

    password=models.CharField(max_length=500)
    def register(self):
        self.save()
    def isExists(self):
        if Customer.objects.filter(email=self.email) or Customer.objects.filter(phone_number=self.phone_number):
            return True
        return False
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_customer_by_phone_number(phone_number):
        try:
            return Customer.objects.get(phone_number=phone_number)
        except:
            return False
    def __str__(self):
        return self.email