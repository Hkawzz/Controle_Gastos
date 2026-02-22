from django import forms
from .models import Gastos

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['nome', 'registro', 'tipo', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input_nome'}),
            'registro': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'input_tipo'}),
            'tipo': forms.Select(attrs={'class': 'input_tipo'}),
            'categoria': forms.TextInput(attrs={'class': 'input_categoria'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
        }