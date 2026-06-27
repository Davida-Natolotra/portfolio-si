from rest_framework import serializers
from .models import IPIdentifier


class IPIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPIdentifier
        fields = "__all__"
