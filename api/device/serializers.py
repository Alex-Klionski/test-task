from rest_framework import serializers
from core.models import Device


class ListDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class AddDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'
