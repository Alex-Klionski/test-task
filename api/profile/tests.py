from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserProfileSerializer
from core.models import UserProfile


class ProfileTests(APITestCase):

    def setUp(self):
        self.user_test1 = User.objects.create_user(username='test', password="1q2w3e")
        self.user_test1.save()
        self.user_test1_token = Token.objects.create(user=self.user_test1)

    def test_valid_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.get(reverse('profile', kwargs={"pk": self.user_test1.id}))
        serializer = UserProfileSerializer(UserProfile.objects.get(user=self.user_test1))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.json())

    def test_invalid_profile(self):
        response = self.client.get(reverse('profile', kwargs={"pk": self.user_test1.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


