from rest_framework import serializers
from core.models import UserProfile


class GetUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ("password", "last_login", "is_active", "is_staff")


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
