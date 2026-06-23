import uuid

from django.db import models

# Create your models here.
class Population(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organisation_unit = models.ForeignKey("organisation_unit.OrganisationUnit", on_delete=models.CASCADE)
    nb_population = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.organisation_unit.name