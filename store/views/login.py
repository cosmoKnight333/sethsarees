from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer

class Login(View):
    def post(self, request):
        email_phone_number = request.POST.get('phone_number')   
        password = request.POST.get('password')   
        next = request.POST.get('next')
        customer = Customer.get_customer_by_email(email_phone_number) or Customer.get_customer_by_phone_number(email_phone_number)
        if customer:
            if check_password(password, customer.password):
                request.session['customer'] = customer.id
                request.session['customer_first_name'] = customer.first_name
                request.session['customer_phone_number'] = customer.phone_number
                return redirect(next)
            else:
                error_msg = "Enter Valid Password"
                return redirect(next + '?error_msg=' + error_msg)
        else:
            error_msg = "Enter Valid Email/Whatsapp Number."
            return redirect(next + '?error_msg=' + error_msg)
