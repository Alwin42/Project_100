from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Connects to your new api/urls.py (Tasks, Reminders, Subjects)
    # This matches http://127.0.0.1:8000/api/tasks/
    path('api/', include('api.urls')), 
    
    # 2. Authentication Endpoints (Keep these!)
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]