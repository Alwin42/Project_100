# App/urls.py

from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings             
from django.conf.urls.static import static   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request/cancel/<int:request_id>/', views.cancel_request, name='cancel_request'),
    path('request/review/<int:request_id>/', views.add_review, name='add_review'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/password/', views.password_change, name='password_change'),
]
# This serves media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)