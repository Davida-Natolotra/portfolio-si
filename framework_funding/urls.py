from rest_framework.routers import DefaultRouter
from .views import FrameworkFundingViewSet

router = DefaultRouter()
router.register("framework-funding", FrameworkFundingViewSet)

urlpatterns = router.urls
