from django import forms
from .models import *


class periodsNursesForm(forms.ModelForm):
    class Meta:
        model = periodsNurses
        fields = '__all__'


class contractsNursesForm(forms.ModelForm):
    class Meta:
        model = contractsNurses
        fields = ['title']


class managementNursesForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'title'}),
        label='Введите наименование учреждения или ФИО организатора группы')

    class Meta:
        model = managementNurses
        fields = '__all__'


class personNursesForm(forms.ModelForm):
    # per_key_period = forms.ModelChoiceField(queryset=periodsNurses.objects.all(),
    #                                         empty_label="--- Выберите период ---",
    #                                         widget=forms.Select(attrs={'class': 'form-control col-12',
    #                                                                    'empty_label': 'disabled'}),
    #                                         label='')
    # per_key_contract = forms.CharField(widget=forms.HiddenInput(), label='')
    # per_key_management = forms.CharField(widget=forms.HiddenInput(), label='')
    # surname = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'id': 'surname'}),
    #     label='Фамилия')
    # name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'id': 'name'}),
    #     label='Имя')
    # patronymic = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control', 'id': 'patronymic'}),
    #     label='Отчество')

    class Meta:
        model = personNurses
        widgets = {'per_key_contract': forms.HiddenInput(),
                   'per_key_management': forms.HiddenInput()}
        fields = '__all__'
