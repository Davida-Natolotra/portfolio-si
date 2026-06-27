from rest_framework import serializers
from .models import DataSourceIndicator


class DataSourceIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSourceIndicator
        fields = "__all__"
