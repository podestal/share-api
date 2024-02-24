from django.contrib.auth.models import User
from share_api.models import Account, Service
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestGetAccounts:

    def test_if_user_anonymus_returns_200(self):
        client = APIClient()
        response = client.get('/api/accounts/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_authenticated_returns_200(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.get('/api/accounts/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_admin_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/accounts/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestGetAccount:

    def test_if_user_anonymus_returns_200(self):
        account = baker.make(Account)
        client = APIClient()
        response = client.get(f'/api/accounts/{account.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == account.id
        assert response.data['username'] == account.username
        assert response.data['password'] == account.password

    def test_if_user_authenticated_returns_200(self):
        account = baker.make(Account)
        client = APIClient()
        client.force_authenticate(user={})
        response = client.get(f'/api/accounts/{account.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == account.id

    def test_if_user_is_admin_returns_200(self):
        account = baker.make(Account)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get(f'/api/accounts/{account.id}/')
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestCreateAccount:

    def test_if_user_anonymus_returns_401(self):
        client = APIClient()
        response = client.post('/api/accounts/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/api/accounts/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_admin_returns_201(self):
        client = APIClient()
        service = baker.make(Service)
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/accounts/', {'username': 'test', 'password': 'test', 'service': service.pk})
        assert response.status_code == status.HTTP_201_CREATED


