from rest_framework.routers import DefaultRouter
from .views import List15ViewSet

router = DefaultRouter()
router.register("list-1-5", List15ViewSet)

urlpatterns = router.urls
