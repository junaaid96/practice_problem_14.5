from django import forms
from .models import anotherModel


class SecondForm(forms.ModelForm):
    class Meta:
        model = anotherModel
        fields = '__all__'
