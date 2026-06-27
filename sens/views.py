from rest_framework.viewsets import ModelViewSet
from .models import Sens
from .serializers import SensSerializer


class SensViewSet(ModelViewSet):
    queryset = Sens.objects.all()
    serializer_class = SensSerializer
