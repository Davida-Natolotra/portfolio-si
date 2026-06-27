from django.db import models
from ip_identifier.models import IPIdentifier


class ReportingPeriod(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Reporting(models.Model):
    ip_id = models.ForeignKey(IPIdentifier, on_delete=models.CASCADE)
    report_period = models.ForeignKey(ReportingPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.report_period)
