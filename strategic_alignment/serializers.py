from rest_framework import serializers
from .models import StrategicAlignment


class StrategicAlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicAlignment
        exclude = ["reporting"]
