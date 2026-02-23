from django import forms
from .models import Entradas

class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['data', 'origem', 'valor']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input_data'}),
            'origem': forms.TextInput(attrs={'class': 'input_origem'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
        }