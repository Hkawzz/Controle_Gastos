from django import forms
from .models import Caixinhas

class CaixinhasForm(forms.ModelForm):
    class Meta:
        model = Caixinhas
        fields = ['objetivo', 'meta', 'guardado']
        widgets = {
            'objetivo': forms.TextInput(attrs={'class': 'input_objetivo'}),
            'meta': forms.NumberInput(attrs={'class': 'input_meta'}),
            'guardado': forms.NumberInput(attrs={'class': 'input_guardado'}),
        }