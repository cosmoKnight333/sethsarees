from django.urls import path
from .views.home import index,logout
from .views.category import show_category
from .views.search import search
from .views.about import show_about
from .views.contact import Contact_Page
from .views.login import Login
from .views.signup import Signup
from .views.detail import Detail
from .views.addtowishlist import addtowishlist



urlpatterns = [
    path('',index,name='homepage'),
    path('category',show_category),
    path('search',search),
    path('logout',logout),
    path('add-to-wishlist',addtowishlist),
    path('contact',Contact_Page.as_view()),
    path('about',show_about),
    path('detail',Detail.as_view()),
    path('login',Login.as_view(),name='login'),
    path('signup',Signup.as_view(),name='signup'),

]