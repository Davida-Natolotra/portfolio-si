from rest_framework.viewsets import ModelViewSet
from .models import IPIdentifier
from .serializers import IPIdentifierSerializer


class IPIdentifierViewSet(ModelViewSet):
    queryset = IPIdentifier.objects.all()
    serializer_class = IPIdentifierSerializer
