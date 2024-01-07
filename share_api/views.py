from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from . import permissions
from . import models
from . import serializers

class ServiceViewSet(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.SerivceSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]

class CredentialsViewSet(ModelViewSet):
    queryset = models.Credentials.objects.all()
    serializer_class = serializers.CredentialsSerializer

class ScreeViewSet(ModelViewSet):
    queryset = models.Screen.objects.all()
    serializer_class = serializers.ScreenSerializer

class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateAccountSerializer
        return serializers.AccountSerializer
    
class CustomerViewSet(ModelViewSet):
    queryset = models.Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.UpdateCustomerSerializer
        return serializers.CustomerSerializer
        

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = models.Customer.objects.get_or_create(user_id=self.request.user.id)
        serializer = serializers.CustomerSerializer(customer)
        return Response(serializer.data)
    

