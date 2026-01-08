from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

@api_view(['GET']) # Only allow reading data, not changing it
def get_cars(request):
    cars = Car.objects.all()          # 1. Get data from DB (Python)
    serializer = CarSerializer(cars, many=True) # 2. Convert to JSON
    return Response(serializer.data)  # 3. Send it to the frontend