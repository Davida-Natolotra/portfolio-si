from django.db import models
from framework_funding.models import FrameworkFunding
from qualitative_analysis.models import QualitativeAnalysis
from risk_matrix.models import RiskMatrixActionPlan
from strategic_alignment.models import StrategicAlignment
from monitoring_technical_performance.models import MonitoringAlignment
from ip_identifier.models import IPIdentifier

class ReportingPeriod(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()



    def __str__(self):
        return self.name


# Create your models here.
class Reporting(models.Model):
    ip_id = models.ForeignKey(IPIdentifier, on_delete=models.CASCADE)
    report_period = models.ForeignKey(ReportingPeriod, on_delete=models.CASCADE)
    framework = models.ForeignKey(FrameworkFunding, on_delete=models.CASCADE)
    strategic_alignment = models.ForeignKey(StrategicAlignment, on_delete=models.CASCADE)
    monitoring_alignment = models.ForeignKey(MonitoringAlignment, on_delete=models.CASCADE)
    qualitative_analysis = models.ForeignKey(QualitativeAnalysis, on_delete=models.CASCADE)
    risk_matrix = models.ForeignKey(RiskMatrixActionPlan, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.report_period)

