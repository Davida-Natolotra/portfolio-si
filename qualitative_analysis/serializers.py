from rest_framework import serializers
from .models import QualitativeAnalysis


class QualitativeAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualitativeAnalysis
        exclude = ["reporting"]
