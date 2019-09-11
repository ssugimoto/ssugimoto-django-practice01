import sys
from unittest import TestCase

from django.test import Client
from django.test import TestCase


# Create your tests here.

class ClientTests(TestCase):
    def test_future_question(self):
        c1 = Client(enforce_csrf_checks=False)
        response = c1.post('/login/', {'username': 'john'})
        status = response.status_code
        print("status=" + str(status))
        self.assertEqual(response.status_code, 404)

    def test_client_post(self):
        c = Client()
        response = c.post('/login/', {'username': 'john'})
        status = response.status_code

        print("status=" + str(status))
        self.assertEqual(response.status_code, 404)
