from rest_framework.viewsets import ModelViewSet
from .models import RiskMatrixActionPlan
from .serializers import RiskMatrixActionPlanSerializer


class RiskMatrixActionPlanViewSet(ModelViewSet):
    queryset = RiskMatrixActionPlan.objects.all()
    serializer_class = RiskMatrixActionPlanSerializer
