from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.wishlist import Wishlist

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'

def search(request):
    customer_id=request.session.get('customer')
    wishlist_len=0
    if customer_id:
        customer=Customer.objects.get(id=customer_id)
        wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
    else:
        print("nothing")
    data['wishlist_len']=wishlist_len

    query=None
    query=request.GET['search']
    categories=Category.get_all_categories()
    p1=Product.objects.filter(description__icontains=query)
    p2=Product.objects.filter(name__icontains=query)
    products=p1.union(p2)
    data['query']="Your search results for : " +query
    data['categories']=categories
    data['products']=products    
    return render(request,'search.html',data)
    
    