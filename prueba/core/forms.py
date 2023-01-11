from .models import ipGenerate
from django import forms

class GeneralForms(forms.ModelForm):
    class Meta:
        model = ipGenerate
        fields = '__all__'