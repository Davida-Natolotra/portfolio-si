from django.db import models
from organisation_unit.models import OrganisationUnit
from area_coop.models import AreaCoop,SubAreaCoop
from technical_area.models import TechnicalArea


# Create your models here.
class FrameworkFunding(models.Model):
    region = models.ForeignKey(OrganisationUnit, on_delete=models.CASCADE, limit_choices_to={'level': 2}, related_name='region_frameworks')
    district = models.ForeignKey(OrganisationUnit, on_delete=models.CASCADE, limit_choices_to={'level': 3}, related_name='district_frameworks')
    technical_area = models.ForeignKey(TechnicalArea,on_delete=models.CASCADE)
    area = models.ForeignKey(AreaCoop,on_delete=models.CASCADE)
    contribution = models.ForeignKey(SubAreaCoop,on_delete=models.CASCADE)
    assigned_funding = models.IntegerField(default=0)

    def __str__(self):
        return str(self.region.name)    