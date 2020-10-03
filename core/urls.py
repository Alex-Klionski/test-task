from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ItemList.as_view(), name="index"),

    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),

    path('edit-avatar/', views.ProfileEditView.as_view(), name="edit-avatar"),
    path('device-add/', views.DeviceCreate.as_view(), name="device-add"),
    path('give-out-device/', views.GiveOutCreate.as_view(), name="give-out-device"),

]