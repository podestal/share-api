from rest_framework import serializers
from core.serializers import UserSerializer
from . import models
from uuid import uuid4
from datetime import date
from core.serializers import UserSerializer

DOLAR_TO_PEN = 3.7

class FeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Feature
        fields = '__all__'

class GetSimpleScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['id', 'available']


class ServiceSerializer(serializers.ModelSerializer):

    screens = GetSimpleScreenSerializer(many=True)
    features = FeaturesSerializer(many=True)

    class Meta:
        model = models.Service
        fields = ['id', 'created_at', 'platform', 'comercial_name', 'screen_limit', 'price', 'screens', 'features']

    
class GetSimpleServiceSerializer(serializers.ModelSerializer):

    one_price = serializers.SerializerMethodField('get_one_month_price')
    three_price = serializers.SerializerMethodField('get_three_month_price')
    six_price = serializers.SerializerMethodField('get_six_month_price')
    nine_price = serializers.SerializerMethodField('get_nine_month_price')

    class Meta:
        model = models.Service
        fields = ['id', 'created_at', 'platform', 'comercial_name', 'screen_limit', 'price', 'one_price', 'three_price', 'six_price', 'nine_price']


    def get_one_month_price(self, service: models.Service):
        return round(float(service.price) * DOLAR_TO_PEN, 2)
    
    def get_three_month_price(self, service: models.Service):
        return round(((float(service.price) * DOLAR_TO_PEN) * 0.97), 2)
    
    def get_six_month_price(self, service: models.Service):
        return round(((float(service.price) * DOLAR_TO_PEN) * 0.94), 2)
    
    def get_nine_month_price(self, service: models.Service):
        return round(((float(service.price) * DOLAR_TO_PEN) * 0.91), 2)


class CreateServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = ['id', 'created_at', 'platform', 'comercial_name', 'screen_limit', 'price',]
    
class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = '__all__'


class GetScreenSerializer(serializers.ModelSerializer):

    service = GetSimpleServiceSerializer()

    class Meta:
        model = models.Screen
        fields = ['id', 'created_at', 'position', 'bulk', 'available', 'service', 'subscribed_at', 'period', 'username', 'password', 'customer', 'due_date']

class CreateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['bulk', 'account']

    def save(self, **kwargs):
        account = self.validated_data.get('account')
        screen_limit = account.service.screen_limit
        service = account.service
        username = account.username
        password = account.password
        if self.validated_data.get('bulk') == True:
            screens = [models.Screen(
                position = screen+1,
                service = service,
                username = username,
                password = password,
                **self.validated_data
            )for screen in range(0, screen_limit)]
            return models.Screen.objects.bulk_create(screens)
        else:
            return models.Screen.objects.create(service = service, username = username, password = password, **self.validated_data)

class UpdateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['available', 'customer', 'period', 'subscribed_at', 'due_date']

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

class CustomerSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'active']

class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['id', 'user']

class UpdateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['active']

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = '__all__'

class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['id', 'screen_id', 'customer_id', 'customer_email', 'screen_username', 'screen_password', 'screen_profile', 'status', 'total', 'days', 'period', 'customer_first_name', 'customer_last_name', 'service_platform']


class OrderReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderReceipt
        fields = ['image']
    
class CreateOrderReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderReceipt
        fields = ['image']

    def create(self, validated_data):
        order_id = self.context['order_id']
        return models.OrderReceipt.objects.create(order_id=order_id, **validated_data)

class UpdateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['status']

class AdminOrderSerializer(serializers.ModelSerializer):

    order_receipt = OrderReceiptSerializer(many=True)

    class Meta:
        model = models.Order
        fields = ['id', 'screen_id', 'customer_id', 'customer_email', 'screen_username', 'screen_password', 'screen_profile', 'days', 'total', 'status', 'period', 'order_receipt', 'customer_first_name', 'customer_last_name', 'service_platform']

