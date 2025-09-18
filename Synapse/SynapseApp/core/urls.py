
from django.contrib import admin
from django.urls import path   
from . import views
urlpatterns = [
    
    path('', views.main),
    path('about/', views.about),
    path('contact/', views.contact),
    path('services/', views.services),
    path('doctors/', views.doctors),
    path('login/', views.login),
    
]
