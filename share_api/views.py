from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import permissions
from . import models
from . import serializers

class ServiceViewSet(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.SerivceSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

class ScreeViewSet(ModelViewSet):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

    def get_serializer_context(self):
        return {'account_id': self.kwargs['accounts_pk']}

class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateAccountSerializer
        return serializers.AccountSerializer
    
class CustomerViewSet(ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
