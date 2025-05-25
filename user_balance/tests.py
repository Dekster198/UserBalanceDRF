from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import User

# Create your tests here.
class UserBalanceTests(APITestCase):
    def setUp(self):
        self.from_user = User.objects.create(username='tester', balance=500)
        self.client_from_user = APIClient()
        self.client_from_user.force_authenticate(user=self.from_user)

        self.to_user = User.objects.create(username='tester2', balance=1000)
        self.client_to_user = APIClient()
        self.client_to_user.force_authenticate(user=self.to_user)

    def test_get_balance(self):
        url = reverse('balance', kwargs={'user_id': User.objects.get(username='tester').id})
        response = self.client_from_user.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deposit(self):
        url = reverse('deposit', kwargs={'user_id': 1})
        data = {'amount': 300}
        response = self.client_from_user.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.from_user.balance + data['amount'], response.data['balance'])
    #
    def test_withdraw(self):
        url = reverse('withdraw', kwargs={'user_id': User.objects.get(username='tester').id})
        data = {'amount': 300}
        response = self.client_from_user.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.from_user.balance - data['amount'], response.data['balance'])

    def test_transfer(self):
        url = reverse('transfer', kwargs={'from_user_id': User.objects.get(username='tester').id})
        data = {'to_user': User.objects.get(username='tester2').id, 'amount': 300}
        response = self.client_from_user.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.from_user.balance - data['amount'], response.data['from_user_balance'])
        self.assertEqual(self.to_user.balance + data['amount'], response.data['to_user_balance'])
