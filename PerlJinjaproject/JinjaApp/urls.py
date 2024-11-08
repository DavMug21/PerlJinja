from django.urls import path
from JinjaApp import views



urlpatterns=[

    path('',views.index,name='my_home'),
    path('about',views.about,name='about_us'),
    path('contact',views.contact,name='my_contact'),
    path('services',views.services,name='my_services'),




]



