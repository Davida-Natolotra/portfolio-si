from rest_framework.viewsets import ModelViewSet
from .models import ActionStatus, ActivityStatus
from .serializers import ActionStatusSerializer, ActivityStatusSerializer


class ActionStatusViewSet(ModelViewSet):
    queryset = ActionStatus.objects.all()
    serializer_class = ActionStatusSerializer


class ActivityStatusViewSet(ModelViewSet):
    queryset = ActivityStatus.objects.all()
    serializer_class = ActivityStatusSerializer
