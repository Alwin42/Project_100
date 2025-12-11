from django.urls import path   
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('appointments/', views.appointment_index, name='appointment_index'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('fees/', views.fee_comparison, name='fee_comparison'),
    path('logout/', views.logout_view, name='logout'), 
    path('labs/', views.lab_list, name='lab_list'),
    path('labs/book/<int:lab_id>/', views.book_lab, name='book_lab'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)