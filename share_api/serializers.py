from rest_framework import serializers
from core.serializers import UserSerializer
from . import models
from uuid import uuid4
from datetime import date
from core.serializers import UserSerializer

class FeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Feature
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    screens = serializers.SerializerMethodField(method_name='get_active_screens')

    class Meta:
        model = models.Service
        fields = ['id', 'created_at', 'platform', 'comercial_name', 'screen_limit', 'price', 'screens']

    def get_active_screens(self, service:models.Service):
        return (models.Screen.objects.filter(service_id = service.id, available=True)).count()
    
class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = '__all__'

    # def save(self, **kwargs):
    #     # screen attr 
    #     # 
    #     platform = self.validated_data.get('service')
    #     service = models.Service.objects.get(platform=platform)
    #     if self.validated_data.get('bulk') == True:
    #         screens = [models.Screen(
    #             **self.validated_data
    #         )for screen in range(0, service.screen_limit)]
    #         return models.Screen.objects.bulk_create(screens)
    #     else:
    #         return models.Screen.objects.create(**self.validated_data)


class GetScreenSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()

    class Meta:
        model = models.Screen
        fields = ['id', 'created_at', 'position', 'bulk', 'available', 'service', 'subscribed_at', 'period', 'username', 'password', 'customer', 'due_date']

class CreateScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Screen
        fields = ['bulk', 'account']

    def save(self, **kwargs):
        # platform = self.validated_data.get('service')
        # service = models.Service.objects.get(platform=platform)
        # if self.validated_data.get('bulk') == True:
        #     screens = [models.Screen(
        #         **self.validated_data
        #     )for screen in range(0, service.screen_limit)]
        #     return models.Screen.objects.bulk_create(screens)
        # else:
        #     return models.Screen.objects.create(**self.validated_data)
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
        fields = ['id', 'status', 'screen', 'service', 'period']

    def create(self, validated_data):
        return models.Order.objects.create(user_id=self.context['user_id'], **validated_data)


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

class OrderSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()
    order_receipt = OrderReceiptSerializer(many=True, read_only=True)
    user = UserSerializer()
    class Meta:
        model = models.Order
        fields = ['id', 'status', 'user', 'screen', 'service', 'order_receipt']

class AdminOrderSerializer(serializers.ModelSerializer):

    service = ServiceSerializer()
    order_receipt = OrderReceiptSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = models.Order
        fields = ['id', 'status', 'period', 'user', 'screen', 'service', 'order_receipt']

