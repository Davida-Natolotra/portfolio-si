from rest_framework.viewsets import ModelViewSet
from .models import OrganisationUnit
from .serializers import OrganisationUnitSerializer


class OrganisationUnitViewSet(ModelViewSet):
    queryset = OrganisationUnit.objects.all()
    serializer_class = OrganisationUnitSerializer
