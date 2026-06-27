from rest_framework.viewsets import ModelViewSet
from .models import DataSourceIndicator
from .serializers import DataSourceIndicatorSerializer


class DataSourceIndicatorViewSet(ModelViewSet):
    queryset = DataSourceIndicator.objects.all()
    serializer_class = DataSourceIndicatorSerializer
