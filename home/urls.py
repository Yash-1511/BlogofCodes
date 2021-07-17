from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.handlesignup,name='signup'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
    path('search/',views.search,name='search'),
]
