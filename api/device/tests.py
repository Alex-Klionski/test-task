from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import ListDeviceSerializer
from core.models import Device


class DeviceTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="Name")

        self.device = Device.objects.create(title="Test device",
                                            comment="Text",
                                            price=68.8,
                                            item_number=45,)
        self.user.save()
        self.device.save()

    def test_device(self):
        self.post = Device.objects.get(title="Test device")
        self.assertEqual(self.post.comment, "Text")

    def test_device_list(self):
        response = self.client.get(reverse("list_device"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
