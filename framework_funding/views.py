from rest_framework.viewsets import ModelViewSet
from .models import FrameworkFunding
from .serializers import FrameworkFundingSerializer


class FrameworkFundingViewSet(ModelViewSet):
    queryset = FrameworkFunding.objects.all()
    serializer_class = FrameworkFundingSerializer
