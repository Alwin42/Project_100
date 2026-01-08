from django.contrib import admin
from django.urls import path, include # <--- Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rentals.urls')), # <--- All rental URLs start with /api/
]