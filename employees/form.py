from django import forms
from .models import *


class LocationChoiceField(forms.Form):
    locations = forms.ModelChoiceField(
        queryset=Employees.objects.values_list("branch", flat=True).distinct(),
        empty_label=None
    )
