from django import forms
from .models import Gastos, Entradas

class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['data', 'origem', 'valor']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['nome', 'registro', 'tipo', 'categoria', 'valor']
        widgets = {
            'registro': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }