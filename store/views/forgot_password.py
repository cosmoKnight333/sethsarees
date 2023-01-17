from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.contact import Contact
from store.models.wishlist import Wishlist
from .data import initial_data
from urllib.parse import urlencode, urlparse 
from urllib.parse import  parse_qs
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
# from twilio.rest import Client
import os
import urllib

# def send_whatsapp_message(phone_number,link):
#     # Your Account Sid and Auth Token from twilio.com/console
#     account_sid = 'AC5146a5e9545497bd6b6c137488f5c47c'
#     auth_token = ''
#     link=link
#     client = Client(account_sid, auth_token)
#     print(phone_number,urllib.parse.unquote(urllib.parse.quote(link)))
#     message = f'''
# Dear valued customer,
# We understand that forgetting a password can be frustrating. Don't worry, it happens to the best of us.
# We are here to help you reset your password and get back on track.
    
# Please tap on the following link to reset your password: 
#     {urllib.parse.unquote(urllib.parse.quote(link))}
    
# If you didn't initiate this password reset, please disregard this message.
    
# Thank you for choosing Seth Sarees,
# The Seth Sarees Team
#     '''
#     to_number = f"whatsapp:{phone_number}"
#     message = client.messages.create(
#         from_='whatsapp:+14155238886',
#         body=message,
#         to=to_number,
#         media_url=['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcZNqhxLLMnq_J1fTIIR-hSqsX4XlpMihPzQ&usqp=CAU'],
#     )

#     if message.sid:
#         return HttpResponse('WhatsApp message sent successfully')
#     else:
#         return HttpResponse('Error Occurred while sending the message')

def send_password_reset_email(email, link):
    subject = 'Password Reset Assistance'
    message = f'''
    <!DOCTYPE html>
    <html>
    <body>
    <h3>Dear valued customer,</h3>
    
    <p>We understand that forgetting a password can be frustrating. Don't worry, it happens to the best of us.</p>
    <p>We are here to help you reset your password and get back on track.</p>
    
    <p>Please click on the button below to reset your password:</p>
    {link}
    <p>If you didn't initiate this password reset, please disregard this email.</p>
    
    <p>Thank you for choosing Seth Sarees,</p>
    <p>The Seth Sarees Team</p>
    </body>
    </html>
   '''
    from_email = 'noreply@example.com'
    recipient_list = [email]
    email = EmailMultiAlternatives(subject, message, from_email, recipient_list,headers={'Message-ID': 'foo'})
    email.attach_alternative(message,'text/html')
    email.send()    
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

def hide_email(email):
    email_parts = email.split("@")
    email_name = email_parts[0]
    email_domain = email_parts[1]

    if len(email_name) > 4:
        email_name = email_name[0:2] + "***" + email_name[-2:]
    else:
        email_name = email_name[0] + "***"

    hidden_email = email_name + "@" + email_domain
    return hidden_email

class Forgot_Password(View):
    def get(self, request):
        data = initial_data
        email=request.GET.get('email')
        data['customer_email']=email
        return render(request, 'forgot_password.html', data)

    def post(self, request):
        data = initial_data
        email = request.POST.get('customer_email')
        customer = Customer.get_customer_by_email(email) or Customer.get_customer_by_phone_number(email)
        is_error=''
        if customer:
            url='/forgot-password'
            url=modify_url(url,'hidden_email',hide_email(customer.email))
            customer_id=customer.id
            link =str(request.build_absolute_uri('/'))
            link=link+'change_password?customer_id='+str(customer.id)+'&customer_verification_token='+customer.verification_token            
            phone_number='+'+customer.country_code+customer.phone_number
            # send_whatsapp_message(phone_number,link)
            return redirect(modify_url(url,'forgot_password_is_error','Success'))
        else:
            url='/forgot-password'
            url=modify_url(url,'email',email)
            return redirect(modify_url(url,'forgot_password_is_error','Error'))