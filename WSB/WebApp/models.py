from django.db import models

class DangerSensor(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    temperaturу = models.FloatField()
    humidity = models.FloatField()

class HomeSensor(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    temperaturу = models.FloatField()
    humidity = models.FloatField()
