from rest_framework import serializers
from core.serializers import UserSerializer
from . import models
from uuid import uuid4

class CredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Credentials
        fields = '__all__'

class SerivceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = '__all__'

class ScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['id', 'created_at', 'bulk', 'available', 'service', 'subscribed_at', 'period', 'username', 'password', 'customer']
    
    def save(self, **kwargs):
        platform = self.validated_data.get('service')
        # username = self.validated_data.get('username')
        # password = self.validated_data.get('password')
        service = models.Service.objects.get(platform=platform)
        # (credentials, created) = models.Credentials.objects.get_or_create(username=username, password=password)
        screens_number = 0
        if self.validated_data.get('bulk') == True:
            if service.platform == 'N' or service.platform == 'D':
                screens_number = 4
            if service.platform == 'H' or service.platform == 'P':
                screens_number = 3
            screens = [models.Screen(
                **self.validated_data
            )for screen in range(0, screens_number)]
            return models.Screen.objects.bulk_create(screens)
        else:
            return models.Screen.objects.create(**self.validated_data, credentials)


class AccountSerializer(serializers.ModelSerializer):

    screens = ScreenSerializer(many=True)

    class Meta:
        model = models.Account
        fields = ['id', 'available', 'created_at', 'platform', 'screen_limit', 'customer', 'screens', 'price']
    
class CreateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = ['platform', 'customer', 'price', 'username', 'password']

    # def save(self, **kwargs):
    #     id = uuid4()
    #     if self.validated_data.get('platform') == 'N':
    #         screen_limit = 5
    #     elif self.validated_data.get('platform') == 'D':
    #         screen_limit = 7
    #     elif self.validated_data.get('platform') == 'H':
    #         screen_limit = 4
    #     account_price = self.validated_data.get('price')
    #     screen_price = (float(account_price)/5) * 1.15
    #     screens = [models.Screen(
    #         available = True,
    #         account_id = id,
    #         price = screen_price
    #     )for screen in range(0, screen_limit)]
    #     account = models.Account.objects.create(id = id, screen_limit= screen_limit, **self.validated_data)
    #     models.Screen.objects.bulk_create(screens)

    #     return account

class CustomerSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    screens = ScreenSerializer(many=True)

    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'active', 'screens']

class UpdateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['active']