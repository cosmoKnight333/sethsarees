from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.contact import Contact
from store.models.wishlist import Wishlist
from .data import initial_data

class Contact_Page(View):
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
        data['title']="Contact Us - Visit Our Showroom or Get in Touch for Wholesale and Retail Orders and Styling Advice"
        return render(request, 'contact.html', data)

    def post(self, request):
        name = request.POST.get('name')   
        whatsapp_number = request.POST.get('whatsapp_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            whatsapp_number=whatsapp_number,
            subject=subject,
            message=message,
        )
        return redirect('homepage')
