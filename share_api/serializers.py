from rest_framework import serializers
from core.serializers import UserSerializer
from . import models
from uuid import uuid4

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = ['id', 'created_at', 'platform', 'screen_limit', 'price']

class GetScreenSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = models.Screen
        fields = ['id', 'created_at', 'bulk', 'available', 'service', 'subscribed_at', 'period', 'username', 'password', 'customer']

class CreateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['bulk', 'available', 'subscribed_at', 'username', 'password', 'service']

class UpdateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['available', 'customer', 'period']

class CustomerSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'active']

class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['user']

class UpdateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['active']