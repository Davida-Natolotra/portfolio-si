from django.db import models

# Create your models here.
class RiskMatrixActionPlan(models.Model):
    risk_identified = models.TextField()
