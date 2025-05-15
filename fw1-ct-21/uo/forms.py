from django import forms
from .models import UE

class UEForm(forms.ModelForm):
    class Meta:
        model = UE
        fields = ['titre', 'description', 'CM', 'TD', 'TP', 'credits', 'formations', 'responsables']
        widgets = {
             'formations': forms.CheckboxSelectMultiple(),
             'responsables': forms.CheckboxSelectMultiple(),
        }
