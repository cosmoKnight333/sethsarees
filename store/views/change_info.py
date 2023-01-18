from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs
from django.contrib.auth.hashers import check_password
import re
# def remove_number_from_sandbox(phone_number:str, account_sid:str, auth_token:str)-> bool:
#     client = Client(account_sid, auth_token)
#     try:
#         # Attempt to retrieve the phone number resource
#         number = client.incoming_phone_numbers(phone_number).fetch()
#         # Remove the phone number from the Sandbox
#         number.delete()
#         return True
#     except TwilioRestException as e:
#         print(e)
#         return False
# def is_number_in_sandbox(phone_number:str, account_sid:str, auth_token:str)-> bool:
#     client = Client(account_sid, auth_token)
#     try:
#         number = client.incoming_phone_numbers(phone_number).fetch()
#         return True
#     except TwilioRestException as e:
#         print(e)
#         return False
      

def email_exists(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return bool(re.search(regex, email))


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

class Change_Info(View):
    def post(self,request):
        url = request.POST.get('next','/')
        postData=request.POST
        first_name=postData.get('first_name')
        last_name=postData.get('last_name')
        phone_number=postData.get('phone_number')
        email=postData.get('email')
        country_code=postData.get('country-code')
        country_code=country_code[1:]            
        password=postData.get('password')
        change_info_error_msg=None
        url=modify_url(url,'error_msg','')
        url=modify_url(url,'signup_error_msg','')
        url=modify_url(url,'change_info_error_msg','')
        customer = Customer.get_customer_by_phone_number(request.session['customer_phone_number'])
        if check_password(password, customer.password):
            if not email_exists(email):
                return redirect(modify_url(url,'change_info_error_msg','Plese Enter Correct Email'))
            complete_phone_number='+'+country_code+phone_number
            complete_old_phone_number='+'+country_code+phone_number
            
            print(complete_phone_number,complete_old_phone_number)
            # if not is_number_in_sandbox(complete_phone_number,'AC5146a5e9545497bd6b6c137488f5c47c',''):
            #     return redirect(modify_url(url,'change_info_error_msg','Plese Enter Verified whatsApp number'))
            # remove_number_from_sandbox('+'+customer.country_code+customer.phone_number,'AC5146a5e9545497bd6b6c137488f5c47c','')
            
            customer.first_name=first_name
            customer.last_name=last_name
            customer.country_code=country_code
            customer.phone_number=phone_number
            customer.email=email      
            customer.save()
            request.session['customer'] = customer.id
            request.session['customer_first_name'] = customer.first_name
            request.session['customer_last_name'] = customer.last_name
            request.session['customer_country_code'] = customer.country_code
            request.session['customer_phone_number'] = customer.phone_number
            request.session['customer_email'] = customer.email
            return redirect(modify_url(url,'change_info_error_msg',''))
        else:
            return redirect(modify_url(url,'change_info_error_msg','Plese Enter Correct Password'))
            