from django.db import models

from area_coop.models import SubAreaCoop


# Create your models here.
class FrameworkFunding(models.Model):
    region = models.ForeignKey('OrganisationUnit',on_delete=models.CASCADE)
    district = models.ForeignKey('OrganisationUnit',on_delete=models.CASCADE)
    technical_area = models.ForeignKey('TechnicalArea',on_delete=models.CASCADE)
    area = models.ForeignKey('AreaCoop',on_delete=models.CASCADE)
    contribution = models.ForeignKey(SubAreaCoop,on_delete=models.CASCADE)
    assigned_funding = models.IntegerField(default=0)

    class Meta:
        db_table = 'framework_funding'

    def __str__(self):
        return str(self.region.name)