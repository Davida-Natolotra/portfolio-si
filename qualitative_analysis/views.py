from rest_framework.viewsets import ModelViewSet
from .models import QualitativeAnalysis
from .serializers import QualitativeAnalysisSerializer


class QualitativeAnalysisViewSet(ModelViewSet):
    queryset = QualitativeAnalysis.objects.all()
    serializer_class = QualitativeAnalysisSerializer
