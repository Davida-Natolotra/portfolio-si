from rest_framework import serializers
from .models import TechnicalArea


class TechnicalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalArea
        fields = "__all__"
