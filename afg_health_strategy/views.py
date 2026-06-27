from rest_framework.viewsets import ModelViewSet
from .models import AFGHealthStrategy
from .serializers import AFGHealthStrategySerializer


class AFGHealthStrategyViewSet(ModelViewSet):
    queryset = AFGHealthStrategy.objects.all()
    serializer_class = AFGHealthStrategySerializer
