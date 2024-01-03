from rest_framework import serializers
from . import models
from uuid import uuid4

class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Screen
        fields = ['available', 'customer', 'price']

    def save(self, **kwargs):
        account_id=self.context['account_id']
        return models.Screen.objects.create(account_id= account_id, **self.validated_data)


class AccountSerializer(serializers.ModelSerializer):

    screens = ScreenSerializer(many=True)

    class Meta:
        model = models.Account
        fields = ['id', 'available', 'created_at', 'platform', 'screen_limit', 'customer', 'screens', 'price']
    
class CreateAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = ['platform', 'customer', 'price']

    def save(self, **kwargs):
        id = uuid4()
        if self.validated_data.get('platform') == 'N':
            screen_limit = 5
        elif self.validated_data.get('platform') == 'D':
            screen_limit = 7
        elif self.validated_data.get('platform') == 'H':
            screen_limit = 4
        account_price = self.validated_data.get('price')
        screen_price = (float(account_price)/5) * 1.15
        screens = [models.Screen(
            available = True,
            account_id = id,
            price = screen_price
        )for screen in range(0, screen_limit)]
        account = models.Account.objects.create(id = id, screen_limit= screen_limit, **self.validated_data)
        models.Screen.objects.bulk_create(screens)

        return account
