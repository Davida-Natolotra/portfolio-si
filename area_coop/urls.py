from rest_framework.routers import DefaultRouter
from .views import AreaCoopViewSet, SubAreaCoopViewSet

router = DefaultRouter()
router.register("area-coop", AreaCoopViewSet)
router.register("sub-area-coop", SubAreaCoopViewSet)

urlpatterns = router.urls
