from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

def show_about(request):
    data = initial_data
    error_msg=None
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg
    customer_id = request.session.get('customer')
    data['wishlist_len']=0
    
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        wishlist_len = len(Wishlist.objects.filter(customer=customer_id))
        data['wishlist_len'] = wishlist_len
    
    data['title']="About Our Shop - Trusted Silk and Banarasi Saree Wholesaler and Retailer in Varanasi Since 1993"
    return render(request, 'about.html', data)
