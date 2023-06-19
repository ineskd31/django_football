from django import forms
from .models import Equipe



class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = '__all__'