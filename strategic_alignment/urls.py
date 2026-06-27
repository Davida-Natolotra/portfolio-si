from rest_framework.routers import DefaultRouter
from .views import StrategicAlignmentViewSet

router = DefaultRouter()
router.register("strategic-alignment", StrategicAlignmentViewSet)

urlpatterns = router.urls
