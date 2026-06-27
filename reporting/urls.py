from rest_framework.routers import DefaultRouter
from .views import ReportingPeriodViewSet, ReportingViewSet

router = DefaultRouter()
router.register("reporting-periods", ReportingPeriodViewSet)
router.register("reporting", ReportingViewSet)

urlpatterns = router.urls
