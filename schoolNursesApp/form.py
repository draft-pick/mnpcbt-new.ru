from django import forms
from .models import *


class periodsAppForm(forms.ModelForm):
    class Meta:
        model = periodsApp
        fields = '__all__'


class contractsAppForm(forms.ModelForm):
    class Meta:
        model = contractsApp
        fields = '__all__'


class managementAppForm(forms.ModelForm):
    class Meta:
        model = managementApp
        fields = '__all__'


class otherAppForm(forms.ModelForm):
    class Meta:
        model = otherApp
        fields = '__all__'
