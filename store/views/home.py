from urllib.parse import parse_qs, urlencode, urlparse
from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.customer import Customer
from store.models.review import Review
from store.models.wishlist import Wishlist
from .data import initial_data
from django.core.mail import send_mail

from django.http import HttpResponse


def modify_url(url, param, value):
    # Parse the URL and retrieve the query string
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    
    # Update the value of the parameter in the query string
    query_dict[param] = value
    
    # Rebuild the URL with the updated query string
    new_query_string = urlencode(query_dict, doseq=True)
    modified_url = parsed_url._replace(query=new_query_string).geturl()
    
    return modified_url

def index(request):
    # send_mail(
    #     'Subject here',  # subject
    #     'Here is the message.',  # message
    #     'sethsarees@gmail.com',  # from_email
    #     ['devkumarseth9@gmail.com'],  # list of recipient email addresses
    #     fail_silently=False,
    # )
    data=initial_data
    customer_id=request.session.get('customer')
    wishlist_len=0
    if customer_id:
        customer=Customer.objects.get(id=customer_id)
        wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
    else:
        print("nothing")
    data['wishlist_len']=wishlist_len
    error_msg=None
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg
    products=Product.get_all_products()
    categories=Category.get_all_categories()
    corousels=Corousel.get_all_corousels()
    reviews=Review.get_all_reviews()
    data['products']=products
    data['categories']=categories
    data['corousels']=corousels
    data['reviews']=reviews
    data['title']="Seth Sarees - Varanasi's Finest Silk and Banarasi Sarees Wholesale & Retail Store - Handwoven and Printed Styles"
    return render(request,'index.html',data)   

def logout(request):
    url=request.GET.get('next')
    request.session.clear()
    url=modify_url(url,'error_msg','')
    url=modify_url(url,'signup_error_msg','')
    url=modify_url(url,'change_info_error_msg','')
    return redirect(url)   
    
