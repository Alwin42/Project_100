from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, auth_send_otp, auth_verify_otp 

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # New Auth Routes
    path('auth/send-otp/', auth_send_otp, name='send-otp'),
    path('auth/verify-otp/', auth_verify_otp, name='verify-otp'),
]