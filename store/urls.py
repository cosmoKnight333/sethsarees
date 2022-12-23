from django.urls import path
from .views.home import index
from .views.category import show_category
from .views.about import show_about
from .views.contact import Contact_Page
from .views.login import Login
from .views.signup import Signup
from .views.detail import Detail



urlpatterns = [
    path('',index,name='homepage'),
    path('category',show_category),
    path('contact',Contact_Page.as_view()),
    path('about',show_about),
    path('detail',Detail.as_view()),
    path('login',Login.as_view(),name="login"),
    path('signup',Signup.as_view(),name="signup"),

]