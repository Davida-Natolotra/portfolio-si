from rest_framework.routers import DefaultRouter
from .views import OrganisationUnitViewSet

router = DefaultRouter()
router.register("organisation-units", OrganisationUnitViewSet)

urlpatterns = router.urls
