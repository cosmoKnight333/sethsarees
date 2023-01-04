from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.wishlist import Wishlist

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'

    
def show_category(request):
    customer_id=request.session.get('customer')
    wishlist_len=0
    if customer_id:
        customer=Customer.objects.get(id=customer_id)
        wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
    else:
        print("nothing")
    data['wishlist_len']=wishlist_len
        
    categoryID=None
    products=Product.get_all_products()
    categories=Category.get_all_categories()
    categoryID= request.GET.get('category')
    category_obj= None
    if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
        category_obj = Category.objects.get(pk=categoryID)
    data['products']=products
    data['categories']=categories
    data['category_obj']=category_obj
    return render(request,'category.html',data)

