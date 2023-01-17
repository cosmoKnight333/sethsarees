from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
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

class Login(View):
    def post(self, request):
        
        email_phone_number = request.POST.get('phone_number')   
        password = request.POST.get('password')   
        url = request.POST.get('next','/')
        next=(str(url))
       
        customer = Customer.get_customer_by_email(email_phone_number) or Customer.get_customer_by_phone_number(email_phone_number)
        url=modify_url(url,'error_msg','')
        url=modify_url(url,'signup_error_msg','')
        url=modify_url(url,'change_info_error_msg','')

        if customer:
            if check_password(password, customer.password):
                request.session['customer'] = customer.id
                request.session['customer_first_name'] = customer.first_name
                request.session['customer_country_code'] = customer.country_code
                request.session['customer_last_name'] = customer.last_name
                request.session['customer_phone_number'] = customer.phone_number
                request.session['customer_email'] = customer.email
                url=modify_url(url,'signup_error_msg','')
                return redirect(modify_url(url,'error_msg',''))
            else:
                url=modify_url(url,'signup_error_msg','')
                error_msg = "Enter Valid Password."
                return redirect(modify_url(url,'error_msg',error_msg))
                
        else:
            url=modify_url(url,'signup_error_msg','')            
            error_msg = "Enter Valid Email/Whatsapp Number."
            return redirect(modify_url(url,'error_msg',error_msg))
