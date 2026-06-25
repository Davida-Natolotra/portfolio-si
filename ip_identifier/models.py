import uuid

from django.db import models

# Create your models here.
class IPIdentifier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ip_name = models.CharField(max_length=50)
    activity_name = models.TextField()
    description = models.TextField()
    period_start = models.DateField()
    period_end = models.DateField()
    budget = models.IntegerField()
    donor = models.CharField(max_length=50)
    version = models.DateField()

    def __str__(self):
        return self.ip_name