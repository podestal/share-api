from django.contrib.auth.models import User
from model_bakery import baker
from share_api.models import Account, Screen, Customer
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestGetScreens:

    def test_if_user_anonymus_returns_200(self):
        client = APIClient()
        response = client.get('/api/screens/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_authenticated_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.get('/api/screens/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_admin_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/screens/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateScreen:

    def test_if_user_anonymus_returns_401(self):
        client = APIClient()
        response = client.post('/api/screens/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_401(self):

        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))   
        response = client.post('/api/screens/')
        print('RESPONSE DATA', response.data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_201(self):

        account = baker.make(Account)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))   
        response = client.post('/api/screens/', {
            'bulk': True,
            'account': account.pk,
        })
        print('RESPONSE DATA', response.data)
        assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
class TestUpdateScreen:

    def test_if_user_anonymus_returns_401(self):
        screen = baker.make(Screen)
        client = APIClient()
        response = client.patch(f'/api/screens/{screen.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_200(self):
        customer = baker.make(Customer)
        screen = baker.make(Screen)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.patch(f'/api/screens/{screen.id}/', {
            'available': False,
            'customer': customer.pk,
            'period': 'T',
            'subscribed_at': '2024-02-17',
            'due_date': '2024-05-17'
        })
        assert response.status_code == status.HTTP_200_OK   

    def test_if_user_is_staff_returns_200(self):
        customer = baker.make(Customer)
        screen = baker.make(Screen)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.patch(f'/api/screens/{screen.id}/', {
            'available': False,
            'customer': customer.pk,
            'period': 'T',
            'subscribed_at': '2024-02-17',
            'due_date': '2024-05-17'
        })
        assert response.status_code == status.HTTP_200_OK