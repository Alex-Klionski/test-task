from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import *
from rest_framework import permissions
from .permissions import IsOwnerProfileOrReadOnly
from core.models import UserProfile
from .serializers import GetUserProfileSerializer, UserProfileSerializer


class GetUserProfileView(ModelViewSet):
    serializer_class = GetUserProfileSerializer
    permissions = [permissions.IsAuthenticated]
    queryset = UserProfile.objects.all()


class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, permissions.IsAuthenticated]