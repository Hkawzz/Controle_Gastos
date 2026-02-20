from django.forms import forms
from .models import Gasto, Entradas

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['nome', 'registro', 'tipo', 'categoria', 'valor']

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['data', 'origem', 'valor']