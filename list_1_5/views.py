from rest_framework.viewsets import ModelViewSet
from .models import List15
from .serializers import List15Serializer


class List15ViewSet(ModelViewSet):
    queryset = List15.objects.all()
    serializer_class = List15Serializer
