from rest_framework.routers import DefaultRouter
from .views import ActionStatusViewSet, ActivityStatusViewSet

router = DefaultRouter()
router.register("action-status", ActionStatusViewSet)
router.register("activity-status", ActivityStatusViewSet)

urlpatterns = router.urls
