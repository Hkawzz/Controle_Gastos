from django import forms
from .models import Fixos

class FixosForm(forms.ModelForm):
    class Meta:
        model = Fixos
        fields = ['nome', 'data', 'tipo', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input_nome'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input_data'}),
            'tipo': forms.Select(attrs={'class': 'input_tipo'}),
            'categoria': forms.TextInput(attrs={'class': 'input_categoria'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
        }