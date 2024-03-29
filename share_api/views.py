from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect   
from datetime import datetime
from django_filters import FilterSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, MultipleChoiceFilter
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
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
    queryset = models.Feature.objects.select_related('service')
    serializer_class = serializers.FeaturesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service']
    filter_class = FeatureFilter

class ServiceViewSet(ModelViewSet):
    queryset = models.Service.objects.prefetch_related('features', 'screens')

    permission_classes = [permissions.IsAdminOrReadOnly]

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateServiceSerializer
        return serializers.ServiceSerializer

class AccountViewSet(ModelViewSet):

    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class ScreenViewSet(ModelViewSet):
    queryset = models.Screen.objects.prefetch_related('service')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['available', 'service', 'customer']
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateScreenSerializer
        if self.request.method == 'PATCH':
            return serializers.UpdateScreenSerializer
        return serializers.GetScreenSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return[AllowAny()]
        if self.request.method in ['POST', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
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
            return models.Customer.objects.select_related('user')
        return models.Customer.objects.filter(user_id=self.request.user.id).select_related('user')
        

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = models.Customer.objects.get_or_create(user_id=self.request.user.id)
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

    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return serializers.UpdateOrderSerializer
        if self.request.user.is_staff:
            return serializers.AdminOrderSerializer

    
    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Order.objects.prefetch_related('order_receipt')

class OrderReceiptViewSet(ModelViewSet):
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateOrderReceiptSerializer
        return serializers.OrderReceiptSerializer

    def get_serializer_context(self):
        return {'order_id': self.kwargs['order_pk']}

    def get_queryset(self):
        return models.OrderReceipt.objects.filter(order_id=self.kwargs['order_pk'])

def say_hello(request, uid, token):
    print(uid)
    print(token)
    # return render(request, 'reset.html', {'uid': uid,'token': token})
    return HttpResponseRedirect(f'http://localhost:5173/reset_new/{uid}/{token}')