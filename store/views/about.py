from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

def show_about(request):
    data = initial_data
    error_msg = request.GET.get('error_msg')
    if error_msg:
        data['error_msg'] = error_msg

    customer_id = request.session.get('customer')
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        wishlist_len = len(Wishlist.objects.filter(customer=customer_id))
        data['wishlist_len'] = wishlist_len

    return render(request, 'about.html', data)
