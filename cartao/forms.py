from django import forms
from .models import Cartao

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['nome', 'data', 'parcela', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input_nome'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input_data'}),
            'parcela': forms.NumberInput(attrs={'class': 'input_parcela'}),
            'categoria': forms.TextInput(attrs={'class': 'input_categoria'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
        }