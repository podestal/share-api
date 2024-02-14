from rest_framework_nested import routers
# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet, basename='customers')
router.register('services', views.ServiceViewSet)
router.register('accounts', views.AccountViewSet, basename='accounts')
router.register('screens', views.ScreeViewSet)
router.register('features', views.FeatureViewSet)
router.register('movies', views.MovieViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

order_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
order_router.register('receipts', views.OrderReceiptViewSet, basename='order-receipts')

urlpatterns = [
    path('password/reset/confirm/<uid>/<token>', views.say_hello)
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view()),
    # path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view()),
] + router.urls + order_router.urls