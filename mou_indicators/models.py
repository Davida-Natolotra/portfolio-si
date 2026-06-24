import uuid

from django.db import models

# Create your models here.
class MOUIndicators(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    indicator_name = models.CharField()
    baseline = models.FloatField()
    year_one = models.IntegerField()
    value_one = models.FloatField()
    year_two = models.IntegerField()
    value_two = models.FloatField()
    year_three = models.IntegerField()
    value_three = models.FloatField()
    year_four = models.IntegerField()
    value_four = models.FloatField()
    year_five = models.IntegerField()
    value_five = models.FloatField()

    def __str__(self):
        return self.indicator_name