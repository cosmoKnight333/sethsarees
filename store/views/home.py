from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.review import Review

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'

 
def index(request):
    products=Product.get_all_products()
    categories=Category.get_all_categories()
    corousels=Corousel.get_all_corousels()
    banaras_photos=BanarasPhoto.get_all_banaras_photos()
    reviews=Review.get_all_reviews()
    data['products']=products
    data['categories']=categories
    data['corousels']=corousels
    data['banaras_photos']=banaras_photos
    data['reviews']=reviews
    print('you are: ',request.session.get('customer_first_name'))
    return render(request,'index.html',data)   

def logout(request):
    request.session.clear()
    return render(request,'index.html',data)   
    
