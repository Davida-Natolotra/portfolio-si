from rest_framework import serializers
from .models import MonitoringAlignment


class MonitoringAlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringAlignment
        exclude = ["reporting"]
