from rest_framework.routers import DefaultRouter
from .views import MonitoringAlignmentViewSet

router = DefaultRouter()
router.register("monitoring-alignment", MonitoringAlignmentViewSet)

urlpatterns = router.urls
