from django.db import models
from django.conf import settings

class Customer(models.Model):
        customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

class Account(models.Model):

    PLATFORM_NETFLIX = 'N'
    PLATFORM_DISNEY = 'D'
    PLATFORM_HBO = 'H'
    PLATFORM_PRIME = 'P'

    PLATFORM_CHOICES = [
        (PLATFORM_NETFLIX, 'Netflix'),
        (PLATFORM_DISNEY, 'Disney'),
        (PLATFORM_HBO, 'Hbo Max'),
        (PLATFORM_PRIME, 'Prime'),
    ]

    id = models.UUIDField(primary_key=True)
    created_at = models.DateField(auto_now=True)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES, default=PLATFORM_NETFLIX)
    available = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    screen_limit = models.SmallIntegerField(default = 3)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Screen(models.Model):
    created_at = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='screens')
    price = models.DecimalField(max_digits=6, decimal_places=2)

