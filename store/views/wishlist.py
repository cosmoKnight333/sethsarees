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
categories=Category.get_all_categories()
data['categories']=categories

def show_wishlist(request):
    customer_id=request.session.get('customer')
    if(customer_id):
        customer=Customer.objects.get(id=customer_id)
        wishlist=Wishlist.objects.filter(customer=customer_id)
        wishlist_len=len(wishlist)
        data['wishlist']=wishlist
        data['wishlist_len']=wishlist_len
        return render(request,'wishlist.html',data)
    else :
        return redirect('pleaselogin')     
        
