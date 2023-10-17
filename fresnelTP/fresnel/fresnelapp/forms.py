from django import forms
from .models import calculo_fresnel

class fresnelForms(forms.ModelForm):
    class meta:
        model = calculo_fresnel
        fields = ['frecuancia', 'distancia']
