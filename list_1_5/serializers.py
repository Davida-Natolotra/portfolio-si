from rest_framework import serializers
from .models import List15


class List15Serializer(serializers.ModelSerializer):
    class Meta:
        model = List15
        fields = "__all__"
