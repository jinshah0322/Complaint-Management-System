from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/dashboard_topic',views.dashboard_topic,name='dashboard_topic'),        
    path('complaint',views.complaint,name='complaint'),
    path('contactus',views.contactus,name='contactus'),
    path('account',views.account,name='account'),
]