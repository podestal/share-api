from django.urls import path
from . import views

urlpatterns = [
    path('password/reset/confirm/<uid>/<token>', views.say_hello)
]