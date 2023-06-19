from django import forms
from .models import Joueur



class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = '__all__'



