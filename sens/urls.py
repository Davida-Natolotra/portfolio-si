from rest_framework.routers import DefaultRouter
from .views import SensViewSet

router = DefaultRouter()
router.register("sens", SensViewSet)

urlpatterns = router.urls
