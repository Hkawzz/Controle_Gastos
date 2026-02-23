from django import forms
from .models import Caixinhas, Dividas

class CaixinhasForm(forms.ModelForm):
    class Meta:
        model = Caixinhas
        fields = ['objetivo', 'meta', 'guardado']
        widgets = {
            'objetivo': forms.TextInput(attrs={'class': 'input_objetivo'}),
            'meta': forms.NumberInput(attrs={'class': 'input_meta'}),
            'guardado': forms.NumberInput(attrs={'class': 'input_guardado'}),
        }

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