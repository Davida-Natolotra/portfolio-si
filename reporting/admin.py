from django.contrib import admin
from .models import Reporting, ReportingPeriod
# Register your models here.
admin.site.register([Reporting,ReportingPeriod])