import smtplib
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs
import urllib
import json

import urllib.parse
import json

def email_exists(email):
    # Set the parameters for the API call
    params = {
        'key': '',
        'format': 'json',
        'email': email
    }

    # Encode the parameters as a query string
    query_string = urllib.parse.urlencode(params)

    # Send a GET request to the API server
    res = urllib.request.urlopen("https://api.mailboxvalidator.com/v1/email/free?" + query_string)

    # Read the response from the API server
    response = res.read()

    # Parse the response as JSON
    result = json.loads(response)
    print(result)
    
    # Check if the email is valid
    if result['is_free'] == 'True':
        return True
    else:
        return False

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
        signup_error_msg=''
        if not email_exists(email):
            signup_error_msg='Please enter valid Email Address.'
            return redirect(modify_url(url,'signup_error_msg',signup_error_msg))
            
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone_number=phone_number,
                            email=email,
                            password=password)
        
        if Customer.isExists(customer):
            signup_error_msg='Email or Phone Number already in Use'
            url=modify_url(url,'error_msg','')
            return redirect(modify_url(url,'signup_error_msg',signup_error_msg))
       
        else :
            customer.password=make_password(customer.password)
            customer.save()
            request.session['customer'] = customer.id
            request.session['customer_first_name'] = customer.first_name
            request.session['customer_last_name'] = customer.last_name
            request.session['customer_phone_number'] = customer.phone_number
            request.session['customer_email'] = customer.email
            url=modify_url(url,'error_msg','')  
            return redirect(modify_url(url,'signup_error_msg',''))