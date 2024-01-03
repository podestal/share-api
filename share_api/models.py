from django.db import models
from django.conf import settings


class Screen(models.Model):
    created_at = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True)

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

    created_at = models.DateField(auto_now=True)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES, default=PLATFORM_NETFLIX)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True)