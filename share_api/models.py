from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=False)

class Service(models.Model):

    created_at = models.DateField(auto_now=True)
    platform = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    screen_limit = models.SmallIntegerField(default = 3)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.platform

class Feature(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


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
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True, related_name='screens')
    subscribed_at = models.DateField(null=True)
    period = models.CharField(max_length=1, choices=PERIOD_CHOICES, default=PERIOD_THREE, null=True, blank=True)
