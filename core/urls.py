from django.urls import path
from . import views

urlpatterns = [
    path('activate/<uid>/<token>', views.activate),
    path('password/reset/confirm/<uid>/<token>', views.reset_password),
]