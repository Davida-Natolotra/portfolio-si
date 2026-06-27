from rest_framework.viewsets import ModelViewSet
from .models import TechnicalArea
from .serializers import TechnicalAreaSerializer


class TechnicalAreaViewSet(ModelViewSet):
    queryset = TechnicalArea.objects.all()
    serializer_class = TechnicalAreaSerializer
