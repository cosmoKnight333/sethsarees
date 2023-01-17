from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from django.db.models import Q
from .data import initial_data

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
def search(request):
    data = initial_data
    customer_id = request.session.get('customer')
    wishlist_len = 0
    data['wishlist_len'] = 0

    if customer_id:
        customer = Customer.objects.get(id=customer_id)
        wishlist_len = len(Wishlist.objects.filter(customer=customer_id))
    data['wishlist_len'] = wishlist_len
    error_msg = None
    error_msg = request.GET.get('error_msg')
    data['error_msg'] = error_msg

    query = request.GET['search']
    categories = Category.get_all_categories()

    # find the closest string matches for the query in the 'name', 'description', 'category__name' and 'category__description' fields
    product_names = Product.objects.values_list('name', flat=True)
    product_name_matches = process.extractBests(query, product_names, score_cutoff=70, limit=12)
    product_names = [match[0] for match in product_name_matches]

    
    category_names = Category.objects.values_list('name', flat=True)
    category_name_matches = process.extractBests(query, category_names, score_cutoff=70, limit=12)    
    category_names = [match[0] for match in category_name_matches]

    
    
    products = Product.objects.filter(
        Q(name__in=product_names) |
        Q(category__name__in=category_names) 
    )

    data['query'] = "Your search results for: " + query
    data['categories'] = categories
    data['products'] = products
    data['title']="Search Sarees - Results for '"+ query+"'"
    return render(request, 'search.html', data)
    