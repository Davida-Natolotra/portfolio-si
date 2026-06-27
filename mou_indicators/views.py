from rest_framework.viewsets import ModelViewSet
from .models import YearIndicators, Indicators, MOUIndicators
from .serializers import YearIndicatorsSerializer, IndicatorsSerializer, MOUIndicatorsSerializer


class YearIndicatorsViewSet(ModelViewSet):
    queryset = YearIndicators.objects.all()
    serializer_class = YearIndicatorsSerializer


class IndicatorsViewSet(ModelViewSet):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer


class MOUIndicatorsViewSet(ModelViewSet):
    queryset = MOUIndicators.objects.all()
    serializer_class = MOUIndicatorsSerializer
