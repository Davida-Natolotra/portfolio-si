from rest_framework.routers import DefaultRouter
from .views import PopulationViewSet

router = DefaultRouter()
router.register("populations", PopulationViewSet)

urlpatterns = router.urls
