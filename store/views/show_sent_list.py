from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data
 
def show_sent_list(request):
    data=initial_data
    customer_id=request.session.get('customer')
    data['wishlist_len']=0
    if(customer_id):
        customer=Customer.objects.get(id=customer_id)
        wishlist=Wishlist.objects.filter(customer=customer_id)
        wishlist_len=len(wishlist)
        data['wishlist_len']=wishlist_len
    else :
        data['wishlist_len']=0
    error_msg=None
    error_msg=request.GET.get('error_msg')
    data['error_msg']=error_msg

    customer_to_show_id=request.GET.get('customer_id')
    wishlist=Wishlist.objects.filter(customer=customer_to_show_id)
    customer_to_show=Customer.objects.get(id=customer_to_show_id)
    data['customer_to_show_name']=customer_to_show.first_name
    data['wishlist']=wishlist        
    return render(request,'show_sent_list.html',data)
