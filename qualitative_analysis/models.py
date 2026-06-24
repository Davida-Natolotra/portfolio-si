from django.db import models

# Create your models here.
class QualitativeAnalysis(models.Model):
    interventions_key_success = models.TextField()
    interventions_bottleneck_factors = models.TextField()

    def __str__(self):
        return self.interventions_key_success