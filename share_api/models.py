from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=False)

class Service(models.Model):

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

    created_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES, default=PLATFORM_NETFLIX)
    available = models.BooleanField(default=True)
    screen_limit = models.SmallIntegerField(default = 3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    screen_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.platform


class Account(models.Model):

    id = models.UUIDField(primary_key=True)
    created_at = models.DateField(auto_now=True)
    Service = models.ForeignKey(Service, on_delete=models.PROTECT)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class Credentials(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Screen(models.Model):

    PERIOD_THREE = 'T'
    PERIOD_SIX = 'S'
    PERIOD_NINE = 'N'

    PERIOD_CHOICES = [
        (PERIOD_THREE, 'Three Months'),
        (PERIOD_SIX, 'Six Months'),
        (PERIOD_NINE, 'Nine Months'),
    ]
    
    created_at = models.DateField(auto_now=True)
    bulk = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    credentials = models.ForeignKey(Credentials, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True, related_name='screens')
    subscribed_at = models.DateField(null=True)
    period = models.CharField(max_length=1, choices=PERIOD_CHOICES, default=PERIOD_THREE, null=True, blank=True)


