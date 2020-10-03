from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:pk>/', views.GetUserProfileView.as_view({'get': 'retrieve', 'put': 'update'})),
    path("<int:pk>/", views.UserProfileDetailView.as_view(), name="profile"),
    path("all/", views.UserProfileListCreateView.as_view(), name="all-profiles"),
]