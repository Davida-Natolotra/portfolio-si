import uuid

from django.db import models

from afg_health_strategy.models import AFGHealthStrategy


# Create your models here.
class StrategicAlignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alignment = models.TextField()
    reason_alignment = models.TextField()
    alignment_AFG_Health = models.ForeignKey(AFGHealthStrategy, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.alignment)
