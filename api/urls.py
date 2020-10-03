from django.urls import path, include, re_path
from rest_framework import permissions

urlpatterns = [
    path('profile/', include('api.profile.urls')),
    path('device/', include('api.device.urls')),
]
