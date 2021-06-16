from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'reg_input'}),
            'name': forms.TextInput(attrs={'class': 'reg_input'}),
            'patronymic': forms.TextInput(attrs={'class': 'reg_input'}),
            'place_job': forms.TextInput(attrs={'class': 'reg_input'}),
            'position': forms.TextInput(attrs={'class': 'reg_input'}),
            'degree': forms.TextInput(attrs={'class': 'reg_input'}),
            'location': forms.TextInput(attrs={'class': 'reg_input'}),
            'phone_job': forms.TextInput(attrs={'class': 'reg_input'}),
            'phone': forms.TextInput(attrs={'class': 'reg_input'}),
            'email': forms.TextInput(attrs={'class': 'reg_input'}),
            'school': forms.Select(attrs={'class': 'reg_input'}),
        }


class RegistrationFormEdit(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
