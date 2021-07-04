from urllib import request

from django import forms
from .models import *


class periodsForm(forms.ModelForm):
    class Meta:
        model = periods
        fields = ['title', 'start_date', 'end_date']


class contractsForm(forms.ModelForm):
    class Meta:
        model = contracts
        fields = '__all__'


class managementForm(forms.ModelForm):
    # man_key_contracts = forms.ModelChoiceField(queryset=contracts.objects.none(),
    #                                            empty_label="--- Выберите контракт ---",
    #                                            widget=forms.Select(attrs={'class': 'form-control col-12',
    #                                                                       'empty_label': 'disabled'}),
    #                                            label='')
    #
    # def __init__(self, *args, **kwargs):
    #     period_app_id1 = kwargs.pop('period_app_id', None)
    #     super(managementForm, self).__init__(*args, **kwargs)
    #     self.fields['man_key_contracts'].queryset = contracts.objects.filter(key_periods=1)
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Введите фамилию *'}),
        initial='Физическое лицо')

    class Meta:
        model = management
        fields = '__all__'


class registrationForm(forms.ModelForm):
    # reg_key_management = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Введите фамилию *'}),
    #     label='')

    class Meta:
        model = form_registration
        fields = ['surname', 'name', 'patronymic', 'birthday', 'sex', 'snils']
        # exclude = ['reg_key_periods', 'reg_key_contract', 'reg_key_management']
