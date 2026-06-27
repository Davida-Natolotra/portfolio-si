from rest_framework.viewsets import ModelViewSet
from .models import StrategicAlignment
from .serializers import StrategicAlignmentSerializer


class StrategicAlignmentViewSet(ModelViewSet):
    queryset = StrategicAlignment.objects.all()
    serializer_class = StrategicAlignmentSerializer
