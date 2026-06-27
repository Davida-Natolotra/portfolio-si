from rest_framework import serializers
from .models import RiskMatrixActionPlan


class RiskMatrixActionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskMatrixActionPlan
        exclude = ["reporting"]
