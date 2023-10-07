from django.contrib import admin

from WebApp.models import DangerSensor
from WebApp.models import HomeSensor

admin.site.register(DangerSensor)
admin.site.register(HomeSensor)