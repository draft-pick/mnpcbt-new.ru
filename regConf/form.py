from django import forms
from .models import *


class regSurnameForm(forms.ModelForm):
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Введите фамилию *'}),
        label='')
    school_key = forms.ModelChoiceField(queryset=schoolName.objects.all(),
                                        empty_label="--- Выберите школу для посещения ---",
                                        widget=forms.Select(attrs={'class': 'form-control col-12',
                                                                   'empty_label': 'disabled'}),
                                        label='')

    class Meta:
        model = regSurname
        fields = ['school_key', 'surname']


class regNameForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Введите имя *'}),
        label='')

    class Meta:
        model = regName
        fields = ['name']


class regPatronymicForm(forms.ModelForm):
    patronymic = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Введите отчество *'}),
        label='')

    class Meta:
        model = regPatronymic
        fields = ['patronymic']


class regOtherForm(forms.ModelForm):
    place_job = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Место работы *'}),
        label='')
    position = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Должность *'}),
        label='')
    degree = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4',
                   'placeholder': 'Ученая степень|Научное звание'}),
        label='',
        required=False)
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Регион *'}),
        label='')
    phone_job = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Рабочий телефон *'}),
        label='')
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Телефон'}),
        label='',
        required=False)
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'E-mail *'}),
        label='')

    class Meta:
        model = regOther
        fields = ['place_job', 'position', 'degree', 'location', 'phone_job', 'phone', 'email']
        widgets = {
        }
