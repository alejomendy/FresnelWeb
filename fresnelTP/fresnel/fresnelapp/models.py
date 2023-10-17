from django.db import models
from django.http import HttpResponse
class calculo_fresnel(models.Model):
    frecuencia = models.FloatField()
    distancia = models.FloatField()