
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('department/', views.department, name='department'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
]
