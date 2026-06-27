from rest_framework.routers import DefaultRouter
from .views import AFGHealthStrategyViewSet

router = DefaultRouter()
router.register("afg-health-strategy", AFGHealthStrategyViewSet)

urlpatterns = router.urls
