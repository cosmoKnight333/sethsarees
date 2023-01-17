from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.wishlist import Wishlist
from .data import initial_data

class Detail(View):
    def get(self, request):
        data = initial_data
        customer_id = request.session.get('customer')
        data['wishlist_len']=0
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
            data['wishlist_len'] = len(Wishlist.objects.filter(customer=customer_id))
        error_msg=None
        error_msg = request.GET.get('error_msg')
        data['error_msg'] = error_msg

        product_id = request.GET.get('product') 
        product_obj=Product.get_product_by_id(product_id)
        data['product_obj'] = product_obj
        data['products'] = Product.get_all_products_by_categoryid_random(product_obj.category.id)
        data['title']="Explore "+ product_obj.name + "- Materials,Fabric quality,Weaving technique,Zari work,Border"
        return render(request, 'detail.html', data)
    
    def post(self, request):
        print(request.build_absolute_uri)
        return redirect('detail')