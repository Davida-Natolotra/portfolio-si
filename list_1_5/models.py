from django.db import models

# Create your models here.
class List15(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.number