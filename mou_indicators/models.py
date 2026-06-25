import uuid
from django.db import models

class YearIndicators(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.PositiveIntegerField()

    def __str__(self):
        return str(self.year)


class Indicators(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    indicator_name = models.CharField()

    def __str__(self):
        return self.indicator_name
# Create your models here.
class MOUIndicators(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year_indicators = models.ForeignKey(YearIndicators, on_delete=models.CASCADE)
    indicator_name = models.ForeignKey(Indicators, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return self.indicator_name

