from django import forms
from pins.models import Pin


class PinForm(forms.ModelForm):
    """Форма создание пина"""
    class Meta:
        model = Pin
        fields = ['img', 'category']
