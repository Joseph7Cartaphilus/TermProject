from django import forms
from pins.models import Pin


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['img', 'category']
