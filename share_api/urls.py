from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet, basename='customers')
router.register('services', views.ServiceViewSet)
router.register('screens', views.ScreeViewSet)
router.register('features', views.FeatureViewSet)
router.register('movies', views.MovieViewSet)
router.register('orders', views.OrderViewSet)

order_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
order_router.register('receipts', views.OrderReceiptViewSet, basename='order-receipts')

# screen_router = routers.NestedDefaultRouter(router, 'accounts', lookup='accounts')
# screen_router.register('screens', views.ScreeViewSet, basename='screens')


urlpatterns = router.urls + order_router.urls