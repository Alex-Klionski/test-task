from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import *
from rest_framework import permissions
from .permissions import IsOwnerProfileOrReadOnly
from core.models import Device
from .serializers import ListDeviceSerializer, AddDeviceSerializer


class DeviceListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Device.objects.all()
    serializer_class = ListDeviceSerializer


class DeviceDetailView(generics.RetrieveAPIView):
    permission_classes = [IsOwnerProfileOrReadOnly, permissions.IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = ListDeviceSerializer


class CreateDeviceView(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = AddDeviceSerializer

    def perform_create(self, serializer):
        serializer.save()


