from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.review import Review
from store.models.wishlist import Wishlist
from .data import initial_data
def index(request):
    data=initial_data
    customer_id=request.session.get('customer')
    wishlist_len=0
    if customer_id:
        customer=Customer.objects.get(id=customer_id)
        wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
    else:
        print("nothing")
    data['wishlist_len']=wishlist_len
    
    products=Product.get_all_products()
    categories=Category.get_all_categories()
    corousels=Corousel.get_all_corousels()
    reviews=Review.get_all_reviews()
    data['products']=products
    data['categories']=categories
    data['corousels']=corousels
    data['reviews']=reviews
    return render(request,'index.html',data)   

def logout(request):
    next=request.GET.get('next')
    request.session.clear()
    return redirect(next)   
    
