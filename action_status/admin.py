from django.contrib import admin
from .models import ActionStatus,ActivityStatus
# Register your models here.
admin.site.register([ActionStatus,ActivityStatus])