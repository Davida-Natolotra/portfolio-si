from django.db import models
from data_source.models import DataSourceIndicator


# Create your models here.
class MonitoringAlignment(models.Model):
    performance_indicator = models.ForeignKey("MOUIndicators", on_delete=models.CASCADE)
    sens = models.ForeignKey("Sens", on_delete=models.CASCADE)
    data_source_indicator = models.ForeignKey("DataSourceIndicator", on_delete=models.CASCADE)
    annual_target = models.FloatField(default=0)
    result_achieved = models.FloatField(default=0)
    achievement_rate = models.FloatField(default=0)
    performance_status = models.FloatField(default=0)
    total_population_covered = models.PositiveIntegerField(default=0)
    total_population_reached = models.PositiveIntegerField(default=0)
    total_population_covered_female = models.PositiveIntegerField(default=0)
    total_population_reached_male = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.performance_indicator)