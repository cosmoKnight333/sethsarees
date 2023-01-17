
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

def show_category(request):
    data = initial_data
    customer_id = request.session.get('customer')
    data['wishlist_len']=0
    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        data['wishlist_len'] = len(Wishlist.objects.filter(customer=customer_id))
    error_msg=''
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg

    category_id = request.GET.get('category')
    if category_id:
        data['products'] = Product.get_all_products_by_categoryid(category_id)
        category_obj=Category.objects.get(pk=category_id)
        data['category_obj'] = category_obj
        data['title']="Saree Category - "+category_obj.name+"- Browse by Fabric, Occasion, or Style"
    else:
        data['title']="Saree Collection - Explore Our Extensive Range of Luxurious Silk and Banarasi Sarees - Wholesale and Retail"
        data['products'] = Product.get_all_products()
        data['categories'] = Category.get_all_categories()
    
    return render(request, 'category.html', data)