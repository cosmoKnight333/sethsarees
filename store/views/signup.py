from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
from urllib.parse import urlencode, urlparse, parse_qs

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
    def get(self, request):
        return render(request, 'signup.html', data)

    def post(self, request):
        url = request.POST.get('next', '/')
        post_data = request.POST

        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        phone_number = post_data.get('phone_number')
        email = post_data.get('email')
        password = post_data.get('password')
        customer = Customer(first_name=first_name, last_name=last_name,
                            phone_number=phone_number, email=email, password=password)

        if Customer.isExists(customer):
            signup_error_msg = 'Email or Phone Number already in use'
            return redirect(modify_url(url, 'signup_error_msg', signup_error_msg))
        else:
            customer.password = make_password(customer.password)
            customer.save()
            err_msg = 'Congratulations on creating an account! Please log in to continue.'
            return redirect('/?error_msg=' + err_msg)
