from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import path, include
from task.models import Task


class BooksTests(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('api/', include('task.urls')),
    ]

    def test_create_book(self):
        """
        Ensure we can create a new task object.
        """
        self.user = User.objects.create_user(username='testuser', password='test12345')
        login = self.client.login(username='testuser', password='test12345')

        url = 'http://localhost:8000/api/task/'
        data = {
            "title": "test",
            "description": "test",
            "execution_period": "2022-06-28T08:56:42Z",
            "executed": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'test')

        url = f'http://localhost:8000/api/task/{Task.objects.get().id}/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'test')

        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'test')
