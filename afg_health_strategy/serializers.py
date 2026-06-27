from rest_framework import serializers
from .models import AFGHealthStrategy


class AFGHealthStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = AFGHealthStrategy
        fields = "__all__"
