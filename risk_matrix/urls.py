from rest_framework.routers import DefaultRouter
from .views import RiskMatrixActionPlanViewSet

router = DefaultRouter()
router.register("risk-matrix", RiskMatrixActionPlanViewSet)

urlpatterns = router.urls
