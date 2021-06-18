from django import forms
from .models import *


class regSurnameForm(forms.ModelForm):
    class Meta:
        model = regSurname
        fields = ['school_key', 'surname']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'reg_input'}),
        }


class regNameForm(forms.ModelForm):
    class Meta:
        model = regName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'reg_input'}),
        }


class regPatronymicForm(forms.ModelForm):
    class Meta:
        model = regPatronymic
        fields = ['patronymic']
        widgets = {
            'patronymic': forms.TextInput(attrs={'class': 'reg_input'}),
        }

