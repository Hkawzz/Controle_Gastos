from django import forms
from .models import Dividas

class DividasForm(forms.ModelForm):
    class Meta:
        model = Dividas
        fields = ['nome', 'data', 'valor', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input_nome'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input_data'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
            'categoria': forms.Select(attrs={'class': 'input_categoria'}),
        }