from django import forms
from .models import Dividas

class DividasForm(forms.ModelForm):
    class Meta:
        model = Dividas
        fields = ['nome', 'valor_parcela', 'total_parcela', 'data']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input_nome'}),
            'valor_parcela': forms.NumberInput(attrs={'class': 'input_valor_parcela'}),
            'total_parcela': forms.NumberInput(attrs={'class': 'input_total_parcela'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input_data'})
        }