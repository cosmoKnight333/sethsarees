import smtplib
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs
import urllib
import secrets
import json
import re
from django.core.mail import EmailMultiAlternatives
def email_exists(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return bool(re.search(regex, email))

# def is_sandbox_participant(phone_number:str, account_sid:str, auth_token:str, service_sid:str) -> bool:
#     client = Client(account_sid, auth_token)
#     try:
#         phone_numbers = client.messaging.services(service_sid).phone_numbers.list()
#         print(phone_numbers)
#         for number in phone_numbers:
#             if number.phone_number == phone_number:
#                 return True
#         return False
#     except Exception as e:
#         print(e)  
#         return False
def modify_url(url, param, value):
    parsed_url = urlparse(url)
    query_dict = parse_qs(parsed_url.query)
    query_dict[param] = value
    new_query_string = urlencode(query_dict, doseq=True)
    modified_url = parsed_url._replace(query=new_query_string).geturl()    
    return modified_url


class Signup(View):
    def post(self,request):
        url = request.POST.get('next','/')
        postData=request.POST
        first_name=postData.get('first_name').capitalize() 
        last_name=postData.get('last_name').capitalize() 
        country_code=postData.get('country-code')
        country_code=country_code[1:]
        phone_number=postData.get('phone_number')
        email=postData.get('email')
        password=postData.get('password')
        verification_token=secrets.token_hex(7)
        error_msg=None
        signup_error_msg=''
        url=modify_url(url,'error_msg','')
        url=modify_url(url,'signup_error_msg','')
        url=modify_url(url,'change_info_error_msg','')
        if not email_exists(email):
            signup_error_msg='Please enter valid Email Address.'
            return redirect(modify_url(url,'signup_error_msg',signup_error_msg))
        complete_phone_number='+'+country_code+phone_number
        print(complete_phone_number)
        # if not is_sandbox_participant(complete_phone_number,'AC5146a5e9545497bd6b6c137488f5c47c','',''):
        #     signup_error_msg='Please enter verified Whatsapp Number.'
        #     return redirect(modify_url(url,'signup_error_msg',signup_error_msg))
            
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone_number=phone_number,
                            email=email,
                            country_code=country_code,
                            password=password,
                            verification_token=verification_token)
        if Customer.isExists(customer):
            signup_error_msg='Email or Phone Number already in Use'
            return redirect(modify_url(url,'signup_error_msg',signup_error_msg))
       
        else :
            customer.password=make_password(customer.password)
            customer.save()
            request.session['customer'] = customer.id
            request.session['customer_first_name'] = customer.first_name
            request.session['customer_last_name'] = customer.last_name
            request.session['customer_phone_number'] = customer.phone_number
            request.session['customer_email'] = customer.email
            request.session['customer_country_code'] = customer.country_code
            return redirect(modify_url(url,'signup_error_msg',''))