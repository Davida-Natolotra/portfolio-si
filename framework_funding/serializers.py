from rest_framework import serializers
from .models import FrameworkFunding


class FrameworkFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrameworkFunding
        exclude = ["reporting"]
