from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data 
def show_wishlist(request):
    data=initial_data
    customer_id=request.session.get('customer')
    if(customer_id):
        customer=Customer.objects.get(id=customer_id)
        wishlist=Wishlist.objects.filter(customer=customer_id)
        wishlist_len=len(wishlist)
        data['wishlist']=wishlist
        data['customer_name']=customer.first_name+customer.last_name
        data['wishlist_len']=wishlist_len
        return render(request,'wishlist.html',data)
    else :
        next = request.GET.get('next', '/')
        url='login?next='+next
        return redirect(url)     
        
