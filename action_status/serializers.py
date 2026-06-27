from rest_framework import serializers
from .models import ActionStatus, ActivityStatus


class ActionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionStatus
        fields = "__all__"


class ActivityStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityStatus
        fields = "__all__"
