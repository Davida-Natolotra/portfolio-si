from rest_framework import serializers
from .models import YearIndicators, Indicators, MOUIndicators


class YearIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearIndicators
        fields = "__all__"


class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        fields = "__all__"


class MOUIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MOUIndicators
        fields = "__all__"
