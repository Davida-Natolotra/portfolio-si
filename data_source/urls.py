from rest_framework.routers import DefaultRouter
from .views import DataSourceIndicatorViewSet

router = DefaultRouter()
router.register("data-source-indicators", DataSourceIndicatorViewSet)

urlpatterns = router.urls
