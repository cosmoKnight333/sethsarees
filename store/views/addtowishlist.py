from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.wishlist import Wishlist

def addtowishlist(request):
    customer_id=request.session.get('customer')
    next = request.POST.get('next', '/')

    if customer_id:
        product_id=request.POST.get('product')
        wishlist_ylen=len(Wishlist.objects.filter(customer=customer_id))
        product=Product.objects.get(id=product_id)
        customer=Customer.objects.get(id=customer_id)
        flag=len(Wishlist.objects.filter(customer=customer_id).filter(product=product_id))
        if flag==0:
            wishlist=Wishlist(customer=customer,
                            product=product)
            wishlist.save()
            return HttpResponseRedirect(next)
        else :
            print('product already in cart')
            return HttpResponseRedirect(next)

    else :
        error_msg='Add products to your wishlist - Login Now!'
        return redirect(next+'&&error_msg='+error_msg)
        

def removeitem(request):
    customer_id=request.session.get('customer')
    next = request.POST.get('next', '/')
    product_id=request.POST.get('product')
    customer_id=request.session.get('customer')
    customer=Customer.objects.get(id=customer_id)
    wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
    instance=Wishlist.objects.filter(customer=customer_id).filter(product=product_id)
    instance.delete()
    return HttpResponseRedirect(next)

    