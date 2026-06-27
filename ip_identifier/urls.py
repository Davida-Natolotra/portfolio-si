from rest_framework.routers import DefaultRouter
from .views import IPIdentifierViewSet

router = DefaultRouter()
router.register("ip-identifiers", IPIdentifierViewSet)

urlpatterns = router.urls
