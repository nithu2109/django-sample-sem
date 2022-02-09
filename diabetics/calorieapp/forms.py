from django import forms
from . models import Calorie

class Calorie_form(forms.ModelForm):
    class Meta:
        model=Calorie
        fields="__all__"