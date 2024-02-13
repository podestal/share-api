from rest_framework_nested import routers
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

# urlpatterns = router.urls + order_router.urls
urlpatterns = [
    path('password/reset/confirm/<uid>/<token>', views.say_hello)
] + router.urls + order_router.urls