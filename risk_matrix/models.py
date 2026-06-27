from django.db import models
from action_status.models import ActionStatus


class RiskMatrixActionPlan(models.Model):
    reporting = models.OneToOneField(
        'reporting.Reporting', on_delete=models.CASCADE, related_name='risk_matrix'
    )
    risk_identified = models.TextField()
    impact = models.PositiveIntegerField()
    probability = models.PositiveIntegerField()
    risk_score = models.PositiveIntegerField()
    risk_level = models.CharField()
    measure_mitigation_proposed = models.CharField()
    main_responsible = models.CharField()
    due_date = models.DateField()
    action_status = models.ForeignKey(ActionStatus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.risk_identified)
