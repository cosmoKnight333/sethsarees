from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'
data['categories']=Category.get_all_categories()


class Detail(View):
    def get(self,request):
        productID= request.GET.get('product') 
        product_obj=Product.get_product_by_id(productID)
        data['product_obj']=product_obj    
        products=Product.get_all_products_by_categoryid(product_obj.category.id)
        data['products']=products    
        return render(request,'detail.html',data)
    def post(self,request):
        print(request.build_absolute_uri)
        return render(request,'detail.html',data)
        
        