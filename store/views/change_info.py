from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
from urllib.parse import urlencode, urlparse
from urllib.parse import  parse_qs
from django.contrib.auth.hashers import check_password

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
        password=postData.get('password')
        change_info_error_msg=None
        customer = Customer.get_customer_by_phone_number(request.session['customer_phone_number'])
        if check_password(password, customer.password):
            customer.first_name=first_name
            customer.last_name=last_name
            customer.phone_number=phone_number
            customer.email=email      
            customer.save()
            request.session['customer'] = customer.id
            request.session['customer_first_name'] = customer.first_name
            request.session['customer_last_name'] = customer.last_name
            request.session['customer_phone_number'] = customer.phone_number
            request.session['customer_email'] = customer.email
            return redirect(modify_url(url,'change_info_error_msg',''))
        else:
            return redirect(modify_url(url,'change_info_error_msg','Plese Enter Correct Password'))
            