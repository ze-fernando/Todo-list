from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from .models import Task
from user.models import User


class TaskTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="teste",
            tel=123,
            age=5,
            password="1234a"
        )

        access_token = AccessToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    def test_list(self):
        res = self.client.get(reverse('list'))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_sucess(self):
        data = {'name': 'Tarefa de Teste', 'done': False, 'user': self.user.id}
        response = self.client.post(reverse('list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_create_fail(self):
        data = {'name': 'Tarefa de Teste', 'done': False}
        res = self.client.post(reverse('list'), data, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_sucess(self):
        task = Task.objects.create(
            name='Tarefa Antiga', done=False, user=self.user)
        data = {'name': 'Nova Tarefa', 'done': True}
        url = reverse('detail', kwargs={'id': task.id})
        res = self.client.put(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertTrue(task.done)

    def test_update_fail(self):
        task = Task.objects.create(
            name='Tarefa Antiga', done=False, user=self.user)
        data = {'name': 'Nova Tarefa'}
        url = reverse('detail', kwargs={'id': task.id})
        res = self.client.put(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_sucess(self):
        task = Task.objects.create(
            name='Tarefa para Excluir', done=False, user=self.user)
        url = reverse('detail', kwargs={'id': task.id})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_delete_fail(self):
        task = Task.objects.create(
            name='Tarefa para Excluir', done=False, user=self.user)
        url = reverse('detail', kwargs={'id': 55})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Task.objects.count(), 1)
