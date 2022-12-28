from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.corousel import Corousel
from .models.banarasphoto import BanarasPhoto
from .models.customer import Customer
from .models.contact import Contact
from .models.review import Review
from .models.wishlist import Wishlist

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category',]

class AdminCorousel(admin.ModelAdmin):
    list_display = ['name','heading','subheading']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
class AdminProduct(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['email']

class AdminBanarasPhoto(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Corousel,AdminCorousel)
admin.site.register(BanarasPhoto,AdminBanarasPhoto)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Wishlist)

