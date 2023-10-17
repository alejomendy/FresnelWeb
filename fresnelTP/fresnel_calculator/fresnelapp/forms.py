from django import forms
from .models import FresnelCalculation

class FresnelCalculationForm(forms.ModelForm):
    class Meta:
        model = FresnelCalculation
        fields = ['frequency', 'distance']
