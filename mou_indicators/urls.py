from rest_framework.routers import DefaultRouter
from .views import YearIndicatorsViewSet, IndicatorsViewSet, MOUIndicatorsViewSet

router = DefaultRouter()
router.register("year-indicators", YearIndicatorsViewSet)
router.register("indicators", IndicatorsViewSet)
router.register("mou-indicators", MOUIndicatorsViewSet)

urlpatterns = router.urls
