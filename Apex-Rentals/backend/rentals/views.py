from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    # This single class handles GET (all), GET (one), POST, PUT, and DELETE
    queryset = Car.objects.all()
    serializer_class = CarSerializer