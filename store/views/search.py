from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from django.db.models import Q

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'


def search(request):
    customer_id = request.session.get('customer')
    wishlist_len = 0
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        wishlist_len = len(Wishlist.objects.filter(customer=customer_id))
    data['wishlist_len'] = wishlist_len
    query = request.GET['search']
    categories = Category.get_all_categories()
    products = Product.objects.filter(
        Q(description__icontains=query) |
        Q(name__icontains=query) |
        Q(category__description__icontains=query) |
        Q(category__name__icontains=query)
    )
    data['query'] = "Your search results for: " + query
    data['categories'] = categories
    data['products'] = products
    return render(request, 'search.html', data)
    