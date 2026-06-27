from rest_framework.viewsets import ModelViewSet
from .models import MonitoringAlignment
from .serializers import MonitoringAlignmentSerializer


class MonitoringAlignmentViewSet(ModelViewSet):
    queryset = MonitoringAlignment.objects.all()
    serializer_class = MonitoringAlignmentSerializer
