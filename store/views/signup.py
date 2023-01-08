from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs

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

class Signup(View):
    def post(self,request):
        url = request.POST.get('next','/')
        postData=request.POST
        first_name=postData.get('first_name')
        last_name=postData.get('last_name')
        phone_number=postData.get('phone_number')
        email=postData.get('email')
        password=postData.get('password')
        error_msg=None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone_number=phone_number,
                            email=email,
                            password=password)
        
        if Customer.isExists(customer):
            signup_error_msg=''
            signup_error_msg='Email or Phone Number already in Use'
            return redirect(modify_url(url,'signup_error_msg',signup_error_msg))
        else :
            customer.password=make_password(customer.password)
            customer.save()
            error_msg='Congratulations on creating an account! Please log in to continue.'
            return redirect(modify_url(url,'error_msg',error_msg))