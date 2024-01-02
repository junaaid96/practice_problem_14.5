import datetime
from django import forms
from django.forms.widgets import NumberInput
from .models import MyModel

birth_year_choice = range(1900, 2021)
colors_choice = [('blue', 'Blue'), ('green', 'Green'), ('red', 'Red')]


class firstForm(forms.Form):
    name = forms.CharField(max_length=50)
    name2 = forms.CharField(max_length=50, label='Your Name', initial='Mr. ')
    email = forms.EmailField(max_length=50)
    email2 = forms.EmailField(
        max_length=50, help_text='Enter a valid email address')
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.Textarea()
    comment3 = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
    agree = forms.BooleanField()
    agree2 = forms.BooleanField(required=False)
    agree3 = forms.BooleanField(label='I agree to the terms and conditions')
    date = forms.DateField()
    date2 = forms.DateField(
        widget=forms.SelectDateWidget(years=birth_year_choice))
    birthdate = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    value = forms.DecimalField(max_digits=5, decimal_places=2)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=colors_choice)
    favorite_colors = forms.MultipleChoiceField(choices=colors_choice)
    favorite_colors2 = forms.MultipleChoiceField(
        choices=colors_choice, widget=forms.CheckboxSelectMultiple)
    favorite_colors3 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=colors_choice)
    model_choice = forms.ModelChoiceField(
        queryset=MyModel.objects.all(), initial=0)
    model_choice2 = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=MyModel.objects.all(),
        initial=0)
    password = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput(render_value = True))
    #validators
    
