from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status

from .models import User


class UserLogin(APITestCase):
    def setUp(self):
        self.usr = User.objects.create_user(
            username="teste",
            tel=123,
            age=5,
            password="1234a"
        )

        self.client = APIClient()

    def test_login_sucess(self):
        url = reverse('login')
        res = self.client.post(
            url,
            {"username": "teste",
             "password": "1234a"}
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_login_fail(self):
        url = reverse('login')
        res = self.client.post(
            url,
            {
                "username": "batata",
                "password": "frita"
            }
        )
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class UserCreate(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_sucess(self):
        initial_count = User.objects.count()
        user = User.objects.create_user(
            username="teste",
            tel=123,
            age=5,
            password="1234a"
        )
        final_count = User.objects.count()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "teste")
        self.assertEqual(final_count, initial_count+1)

    def test_create_fail(self):
        initial_count = User.objects.count()
        with self.assertRaises(ValueError):
            user = User.objects.create_user(
                username="",
                tel=123,
                age="a",
                password="1234a"
            )
        final_count = User.objects.count()
        self.assertEqual(final_count, initial_count)
