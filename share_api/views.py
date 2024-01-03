from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class ScreeViewSet(ModelViewSet):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer 
