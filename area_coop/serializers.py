from rest_framework import serializers
from .models import AreaCoop, SubAreaCoop


class AreaCoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaCoop
        fields = "__all__"


class SubAreaCoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAreaCoop
        fields = "__all__"
