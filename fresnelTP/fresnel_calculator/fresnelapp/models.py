from django.db import models

class FresnelCalculation(models.Model):
    frequency = models.FloatField()
    distance = models.FloatField()
