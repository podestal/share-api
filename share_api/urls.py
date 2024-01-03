from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('screens', views.ScreeViewSet)
router.register('accounts', views.AccountViewSet)

urlpatterns = router.urls