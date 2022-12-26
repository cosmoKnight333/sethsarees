from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer
data={}
class Login(View):
    def get(self,request):
        return render(request,'login.html',data)     
    def post(self,request):
        email_phone_number = request.POST.get('phone_number')   
        password = request.POST.get('password')   
        customer=Customer.get_customer_by_email(email_phone_number)
        error_msg= None
        if customer:
            flag=check_password(password,customer.password) 
            if flag:
                request.session['customer']=customer.id
                request.session['customer_first_name']=customer.first_name
                request.session['customer_phone_number']=customer.phone_number
                return redirect('homepage')
            else :
                error_msg="Enter Valid Password"
                data['error_msg']=error_msg
                return render(request,'login.html',data)     
        else :
            error_msg=None
            customer=Customer.get_customer_by_phone_number(email_phone_number)
            if customer:
                flag=check_password(password,customer.password) 
                if flag:
                    request.session['customer']=customer.id
                    request.session['customer_first_name']=customer.first_name
                    request.session['customer_phone_number']=customer.phone_number
                    
                    return redirect('homepage')
                else :
                    error_msg="Enter Valid Password" 
                    data['error_msg']=error_msg       
                    return render(request,'login.html',data)    
            else :
                error_msg="Enter Valid Email/Whatsapp Number."
                data['error_msg']=error_msg
                return render(request,'login.html',data)     
