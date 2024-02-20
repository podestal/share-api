from django.db import models
from django.conf import settings

class Customer(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

class Service(models.Model):

    created_at = models.DateField(auto_now=True)
    platform = models.CharField(max_length=255)
    comercial_name = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    screen_limit = models.SmallIntegerField(default = 3)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.platform

class Feature(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True, related_name='features')

class Account(models.Model):

    created_at = models.DateField(auto_now=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Screen(models.Model):

    PERIOD_ONE = 'O'
    PERIOD_THREE = 'T'
    PERIOD_SIX = 'S'
    PERIOD_NINE = 'N'

    PERIOD_CHOICES = [
        (PERIOD_ONE, 'One Month'),
        (PERIOD_THREE, 'Three Months'),
        (PERIOD_SIX, 'Six Months'),
        (PERIOD_NINE, 'Nine Months'),
    ]
    
    created_at = models.DateField(auto_now=True)    
    bulk = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    position = models.SmallIntegerField(null=True, blank=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='screens')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name='screens')
    subscribed_at = models.DateField(null=True, blank=True)
    period = models.CharField(max_length=1, choices=PERIOD_CHOICES, default=PERIOD_THREE, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

class Movie(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    services = models.ForeignKey(Service, on_delete=models.PROTECT)

class Order(models.Model):

    STATUS_STARTED = 'S'
    STATUS_PROCESSING = 'P'
    STATUS_COMPLETED = 'C'

    STATUS_CHOICES = [
        (STATUS_STARTED, 'Started'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_COMPLETED, 'Completed'),
    ]
    
    createdAt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_STARTED)
    screen = models.ForeignKey(Screen, on_delete=models.PROTECT, null=True)
    period = models.CharField(max_length=1)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    days = models.SmallIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    total = models.DecimalField(max_digits=6, decimal_places=2)

class OrderReceipt(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_receipt')
    image = models.ImageField(upload_to='api/images',)

