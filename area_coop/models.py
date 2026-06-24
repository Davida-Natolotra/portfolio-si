import uuid

from django.db import models

# Create your models here.
class AreaCoop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubAreaCoop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.ForeignKey(AreaCoop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name