from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.DeviceDetailView.as_view(), name="detail_device"),
    path('all/', views.DeviceListView.as_view(), name="list_device"),
    path('add-device/', views.CreateDeviceView.as_view(), name="add_device"),
]