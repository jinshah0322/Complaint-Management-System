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
    path('dashboard/dashboard_water',views.dashboard_water,name='dashboard_water'),        
    path('dashboard/dashboard_light',views.dashboard_light,name='dashboard_light'),        
    path('dashboard/dashboard_clean',views.dashboard_clean,name='dashboard_clean'),        
    path('dashboard/dashboard_other',views.dashboard_other,name='dashboard_other'),        
    path('complaint',views.complaint,name='complaint'),
    path('contactus',views.contactus,name='contactus'),
    path('account/<str:pk>',views.account,name='account'),
    path('contactform',views.form,name='form'),
    path('complaintform',views.complaintform,name='complaintform'),
    path('admins',views.admin,name='admin'),
    path('yes/<str:pk>',views.yes,name='yes'),
    path('no/<str:pk>',views.no,name='no'),
    path('query',views.query,name='query'),
    path('oldcomplaints',views.oldcomplaints,name='oldcomplaints'),
]