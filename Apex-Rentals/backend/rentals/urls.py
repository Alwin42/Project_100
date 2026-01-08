from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

# Create a router and register our ViewSet with it.
router = DefaultRouter()
router.register(r'cars', CarViewSet) 
# The 'r'cars'' argument means the URL prefix will be /cars/

urlpatterns = [
    path('', include(router.urls)),
]