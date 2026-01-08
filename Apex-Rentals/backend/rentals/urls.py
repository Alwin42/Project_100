from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.get_cars), # The address is http://.../api/cars/
]