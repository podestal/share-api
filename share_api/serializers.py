from rest_framework import serializers
from . import models

class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Screen
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'