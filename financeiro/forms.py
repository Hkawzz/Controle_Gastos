from django import forms
from .models import Entradas, Fixos, Cartao, Caixinhas, Dividas

class EntradasForm(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['data', 'origem', 'valor']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'input_data'}),
            'origem': forms.TextInput(attrs={'class': 'input_origem'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
        }

class FixosForm(forms.ModelForm):
    class Meta:
        model = Fixos
        fields = ['nome', 'data', 'tipo', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'date', 'class': 'input_nome'}),
            'data': forms.DateInput(attrs={'class': 'input_data'}),
            'tipo': forms.Select(attrs={'class': 'input_tipo'}),
            'categoria': forms.TextInput(attrs={'class': 'input_categoria'}),
            'valor': forms.NumberInput(attrs={'class': 'input_valor'}),
        }

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