from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer
data={}
class Signup(View):
    def get(self,request):
        return render(request,'signup.html',data)
    def post(self,request):
        postData=request.POST
        first_name=postData.get('first_name')
        last_name=postData.get('last_name')
        phone_number=postData.get('phone_number')
        email=postData.get('email')
        password=postData.get('password')
        error_msg=None
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_name': phone_number,
            'email': email
        }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone_number=phone_number,
                            email=email,
                            password=password)
        
        if Customer.isExists(customer):
            data['values']=values
            error_msg="Email or Phone Number Already in Use"
            data['error_msg']=error_msg
            return render(request,'signup.html',data)
        else :
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('login')
