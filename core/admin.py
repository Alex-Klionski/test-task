from django.contrib import admin
from .models import UserProfile, Device

admin.site.register(UserProfile)
admin.site.register(Device)
