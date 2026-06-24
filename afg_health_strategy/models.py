import uuid

from django.db import models

# Create your models here.
class AFGHealthStrategy(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name