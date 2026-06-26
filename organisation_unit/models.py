from django.db import models


class OrganisationUnit(models.Model):
    id = models.CharField(primary_key=True, max_length=50, editable=False)
    code = models.CharField(max_length=50, blank=True, default="")
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    created = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0)
    path = models.CharField(max_length=500)
    geometry = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name