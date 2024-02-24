from django.contrib.auth.models import User
from model_bakery import baker
from share_api.models import Customer, Service
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestGetOrders:

    def test_if_user_anonymus_returns_401(self):
        client = APIClient()
        response = client.get('/api/orders/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_401(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.get('/api/orders/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/orders/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateOrders:

    def test_if_user_anonymus_returns_401(self):
        client = APIClient()
        response = client.post('/api/orders/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_201(self):

        customer = baker.make(Customer)
        service = baker.make(Service)

        client = APIClient()
        client.force_authenticate(user=User)   
        response = client.post('/api/orders/', {
            'total': 45.00,
            'customer': customer.pk,
            'service': service.pk,
            'days': 90,
            'period': 'T'
        })
        print('RESPONSE DATA', response.data)
        assert response.status_code == status.HTTP_201_CREATED
