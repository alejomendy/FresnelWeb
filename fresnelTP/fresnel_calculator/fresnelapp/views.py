from django.shortcuts import render
from .forms import FresnelCalculationForm
import math

def calculate_fresnel_zone(distance, frequency):
    wavelength = 300 / frequency  # Speed of light / frequency in MHz
    radius = math.sqrt((wavelength * distance) / 2)
    return radius

def fresnel_calculator(request):
    if request.method == 'POST':
        form = FresnelCalculationForm(request.POST)
        if form.is_valid():
            frequency = form.cleaned_data['frequency']
            distance = form.cleaned_data['distance']
            fresnel_zone = calculate_fresnel_zone(distance, frequency)
            return render(request, 'fresnelapp/result.html', {'fresnel_zone': fresnel_zone})
    else:
        form = FresnelCalculationForm()
    return render(request, 'fresnelapp/calculate.html', {'form': form})
