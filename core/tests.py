from decimal import Decimal

from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Device, UserProfile


class DeviceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="abc")

        self.device = Device.objects.create(title="Test device",
                                            comment="Text",
                                            price=68.8,
                                            item_number=45, )

    def test_title(self):
        device = Device.objects.get(title="Test device")
        self.assertEqual(device.title, "Test device")

    def test_price(self):
        device = Device.objects.get(title="Test device")
        self.assertEqual(device.item_number, 45)



