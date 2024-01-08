from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from . import permissions
from . import models
from . import serializers

class ServiceViewSet(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class ScreeViewSet(ModelViewSet):
    queryset = models.Screen.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['available', 'service']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateScreenSerializer
        if self.request.method == 'PUT':
            return serializers.UpdateScreenSerializer
        return serializers.GetScreenSerializer

    
class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateCustomerSerializer
        if self.request.method == 'PUT':
            return serializers.UpdateCustomerSerializer
        return serializers.CustomerSerializer
    
    def get_queryset(self):
        return models.Customer.objects.filter(user_id=self.request.user.id)
        

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = models.Customer.objects.get_or_create(user_id=self.request.user.id)
        serializer = serializers.CustomerSerializer(customer)
        return Response(serializer.data)
    

