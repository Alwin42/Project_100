from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
]