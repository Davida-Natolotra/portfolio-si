from rest_framework.routers import DefaultRouter
from .views import QualitativeAnalysisViewSet

router = DefaultRouter()
router.register("qualitative-analysis", QualitativeAnalysisViewSet)

urlpatterns = router.urls
