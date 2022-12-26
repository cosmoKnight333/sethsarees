from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'

 
def addtowishlist(request):
    next = request.POST.get('next', '/')
    product=request.POST.get('product')
    wishlist=request.session.get('wishlist')
    if wishlist:
        wishlist[product]=1
        
    else:
        wishlist={}
        wishlist[product]=1
    print(wishlist)
    request.session['wishlist']=wishlist
    return HttpResponseRedirect(next)