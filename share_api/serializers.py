from rest_framework import serializers
from core.serializers import UserSerializer
from . import models
from uuid import uuid4

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = '__all__'

class GetScreenSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = models.Screen
        fields = ['id', 'created_at', 'bulk', 'available', 'service', 'subscribed_at', 'period', 'username', 'password', 'customer']

class CreateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['id', 'created_at', 'bulk', 'available', 'subscribed_at', 'period', 'username', 'password', 'customer', 'service']
    
    def save(self, **kwargs):
        platform = self.validated_data.get('service')
        service = models.Service.objects.get(platform=platform)
        if self.validated_data.get('bulk') == True:
            screens = [models.Screen(
                **self.validated_data
            )for screen in range(0, service.screen_limit)]
            return models.Screen.objects.bulk_create(screens)
        else:
            return models.Screen.objects.create(**self.validated_data)

class UpdateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['available', 'username', 'password', 'customer', 'period']

# class CreateAccountSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.Account
#         fields = ['platform', 'customer', 'price', 'username', 'password']

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
    screens = ServiceSerializer(many=True)

    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'active', 'screens']

class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['user']

class UpdateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['active']