from rest_framework.viewsets import ModelViewSet
from .models import ReportingPeriod, Reporting
from .serializers import ReportingPeriodSerializer, ReportingSerializer


class ReportingPeriodViewSet(ModelViewSet):
    queryset = ReportingPeriod.objects.all()
    serializer_class = ReportingPeriodSerializer


class ReportingViewSet(ModelViewSet):
    queryset = Reporting.objects.all()
    serializer_class = ReportingSerializer
