from django.contrib import admin
from .models import UserProfile, WasteType, CollectionRequest, IllegalDumpingReport

# This tells the admin site to show these models
admin.site.register(UserProfile)
admin.site.register(WasteType)
admin.site.register(CollectionRequest)
admin.site.register(IllegalDumpingReport)