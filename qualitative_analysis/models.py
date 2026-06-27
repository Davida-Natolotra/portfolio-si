from django.db import models


class QualitativeAnalysis(models.Model):
    reporting = models.OneToOneField(
        'reporting.Reporting', on_delete=models.CASCADE, related_name='qualitative_analysis'
    )
    interventions_key_success = models.TextField()
    interventions_bottleneck_factors = models.TextField()

    def __str__(self):
        return self.interventions_key_success
