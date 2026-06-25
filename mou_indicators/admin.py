from django.contrib import admin
from .models import MOUIndicators,YearIndicators, Indicators
# Register your models here.
admin.site.register([MOUIndicators,YearIndicators,Indicators])