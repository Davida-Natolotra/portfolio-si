import uuid

from django.db import models

# Create your models here.
class OrganisationUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name