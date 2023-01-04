from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.corousel import Corousel
from store.models.banarasphoto import BanarasPhoto
from store.models.customer import Customer
from store.models.contact import Contact
from store.models.wishlist import Wishlist

data={}
data['address']='Ck 13/14 Satti Chautra Chowk Varanasi'
data['phone_no']='918957451402'
data['email']='sethsarees@gmail.com'
categories=Category.get_all_categories()
data['categories']=categories

class Contact_Page(View):
    def get(self,request):
        customer_id=request.session.get('customer')
        wishlist_len=0
        if customer_id:
            customer=Customer.objects.get(id=customer_id)
            wishlist_len=len(Wishlist.objects.filter(customer=customer_id))
        else:
            print("nothing")
        data['wishlist_len']=wishlist_len
                

        return render(request,'contact.html',data)


    def post(self,request):
        name = request.POST.get('name')   
        whatsapp_number = request.POST.get('whatsapp_number')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact =Contact()
        contact.name=name
        contact.whatsapp_number=whatsapp_number
        contact.subject=subject
        contact.message=message
        contact.save()
        return redirect('homepage')
        
           
