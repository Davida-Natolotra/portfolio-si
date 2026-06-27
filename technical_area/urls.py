from rest_framework.routers import DefaultRouter
from .views import TechnicalAreaViewSet

router = DefaultRouter()
router.register("technical-areas", TechnicalAreaViewSet)

urlpatterns = router.urls
