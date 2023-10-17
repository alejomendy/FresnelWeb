from django.shortcuts import render
from .forms import calculo_fresnel
import math
from . import models


    

def calcular_zona(frecuencia,distancia):
    d1 = ((distancia)/(frecuencia))
    raiz = math.sqrt(d1)
    radio = (8.65*(raiz))
    return radio
def main_page(request):
    if request.method == 'POST':
        form = calculo_fresnel(request.POST)
        if form.is_valid():
            frecuencia = form.cleaned_data['frecuencia']
            distancia = form.cleaned_data['distancia']
            zona_fresnel = calcular_zona(distancia,frecuencia)
            return render(request, 'app/calcular.html',{'zona_fresnel': zona_fresnel})
    else:
        form = calculo_fresnel()
    return render(request, 'app/resultado.html',{'form' : form}) 

def prueba(request):
    return render(request,'app/calcular.html')