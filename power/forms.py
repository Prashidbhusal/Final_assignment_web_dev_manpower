from django import forms
from .models import *
from django.forms import ModelForm, Textarea


class FormVacancy(forms.ModelForm):
    
    class Meta():
        model = VacancyForm
        fields = ('__all__')
        exclude= ['user', 'vacancy','applied', 'response','seen']
        widgets = {
            'qualification': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        