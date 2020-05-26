import json
from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import PersonSerializer,ProfessionSerializer
from .models import Profession,Person

# Create your tests here.
class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"profession_name" : "保育園","income" : "2000","weekly_holiday" : "週休1日"}
        response = self.client.post("/profession/",data)
        print(data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
