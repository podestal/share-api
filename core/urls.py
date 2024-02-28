from django.urls import path
from . import views

urlpatterns = [
    path('payment_confirmation/<email>/<username>/<password>/<profile>', views.payment_confirmation),
    path('activate/<uid>/<token>', views.activate),
    path('password/reset/confirm/<uid>/<token>', views.reset_password),
]