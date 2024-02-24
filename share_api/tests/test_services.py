from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestGetService:

    def test_if_user_anonymus_returns_200(self):
        client = APIClient()
        response = client.get('/api/services/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_authenticated_returns_200(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.get('/api/services/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_admin_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/services/')
        assert response.status_code == status.HTTP_200_OK

class TestCreateService:

    def test_if_user_anonymus_returns_401(self):
        client = APIClient()
        response = client.post('/api/services/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/api/services/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_platform_is_blank_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/services/', {'platform': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['platform'] is not None

    def test_if_comercial_name_is_blank_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/services/', {'comercial_name': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['comercial_name'] is not None
    
    def test_if_screen_limit_is_blank_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/services/', {'screen_limit': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_price_is_blank_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/services/', {'price': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['price'] is not None
