from rest_framework import serializers
from .models import Sens


class SensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sens
        fields = "__all__"
