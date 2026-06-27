from rest_framework.viewsets import ModelViewSet
from .models import AreaCoop, SubAreaCoop
from .serializers import AreaCoopSerializer, SubAreaCoopSerializer


class AreaCoopViewSet(ModelViewSet):
    queryset = AreaCoop.objects.all()
    serializer_class = AreaCoopSerializer


class SubAreaCoopViewSet(ModelViewSet):
    queryset = SubAreaCoop.objects.all()
    serializer_class = SubAreaCoopSerializer
