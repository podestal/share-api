from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('accounts', views.AccountViewSet)
router.register('customers', views.CustomerViewSet)
router.register('services', views.ServiceViewSet)
router.register('screens', views.ScreeViewSet)
router.register('credentails', views.CredentialsViewSet)

# screen_router = routers.NestedDefaultRouter(router, 'accounts', lookup='accounts')
# screen_router.register('screens', views.ScreeViewSet, basename='screens')


urlpatterns = router.urls 