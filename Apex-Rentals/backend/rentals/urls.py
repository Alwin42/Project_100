from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

# Create the router and register the 'cars' endpoint
router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    # This includes the router URLs (e.g., /cars/, /cars/1/)
    path('', include(router.urls)),
]