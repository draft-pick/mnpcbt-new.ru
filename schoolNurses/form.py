from django import forms
from .models import *


class periodsForm(forms.ModelForm):
    class Meta:
        model = periods
        fields = ['title']


class managementForm(forms.ModelForm):

    class Meta:
        model = management
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__()
    #     user = kwargs.pop('user', '')
    #     super(managementForm, self).__init__(*args, **kwargs)
    #     self.fields['man_key_periods'] = forms.ModelChoiceField(queryset=periods.objects.filter(man_period_fk=user))
    #


class registrationForm(forms.ModelForm):
    reg_key_contract = forms.ModelChoiceField(queryset=contracts.objects.all(),
                                              empty_label="--- Выберите контракт ---",
                                              widget=forms.Select(attrs={'class': 'form-control col-12',
                                                                         'empty_label': 'disabled'}),
                                              label='')
    reg_key_management = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control col-12 col-md-3 offset-md-1 my-4', 'placeholder': 'Введите имя *'}),
        label='')

    class Meta:
        model = form_registration
        fields = ['reg_key_periods', 'reg_key_contract', 'surname', 'name', 'patronymic',
                  'birthday', 'sex', 'snils']
