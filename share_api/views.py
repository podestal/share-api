from django.shortcuts import render
from datetime import datetime
from django_filters import FilterSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, MultipleChoiceFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from . import permissions
from . import models
from . import serializers

class FeatureFilter(FilterSet):

    service = MultipleChoiceFilter(
        name = 'service',
    )

    class Meta:
        model = models.Feature
        fields = '__all__'

class FeatureViewSet(ModelViewSet):
    queryset = models.Feature.objects.all()
    serializer_class = serializers.FeaturesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service']
    filter_class = FeatureFilter

class ServiceViewSet(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class ScreeViewSet(ModelViewSet):
    queryset = models.Screen.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['available', 'service', 'customer']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateScreenSerializer
        if self.request.method == 'PUT':
            return serializers.UpdateScreenSerializer
        return serializers.GetScreenSerializer

    
class CustomerViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'delete', 'post']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateCustomerSerializer
        if self.request.method == 'PUT':
            return serializers.UpdateCustomerSerializer
        return serializers.CustomerSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Customer.objects.all()
        return models.Customer.objects.filter(user_id=self.request.user.id)
        

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        print('user id',self.request.user.id)
        customer = models.Customer.objects.get(user_id=self.request.user.id)
        print('customers', customer)
        serializer = serializers.CustomerSerializer(customer)
        return Response(serializer.data)
    
class MovieViewSet(ModelViewSet):

    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    

class OrderViewSet(ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    # ordering_fields = ['status']

    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return serializers.UpdateOrderSerializer
        if self.request.user.is_staff:
            return serializers.AdminOrderSerializer
        return serializers.OrderSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Order.objects.all()
        return models.Order.objects.filter(user_id=self.request.user.id)

class OrderReceiptViewSet(ModelViewSet):
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderReceiptSerializer
        return serializers.OrderReceiptSerializer

    def get_serializer_context(self):
        return {'order_id': self.kwargs['order_pk']}

    def get_queryset(self):
        return models.OrderReceipt.objects.filter(order_id=self.kwargs['order_pk'])
