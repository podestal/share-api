from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('accounts', views.AccountViewSet)

screen_router = routers.NestedDefaultRouter(router, 'accounts', lookup='accounts')
screen_router.register('screens', views.ScreeViewSet, basename='screens')


urlpatterns = router.urls + screen_router.urls