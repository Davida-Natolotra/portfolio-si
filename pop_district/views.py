from rest_framework.viewsets import ModelViewSet
from .models import Population
from .serializers import PopulationSerializer


class PopulationViewSet(ModelViewSet):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer
