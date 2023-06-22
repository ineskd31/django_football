from django import forms
from .models import Joueur
from equipe.models import Equipe



class JoueurForm(forms.ModelForm):
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), required=False)
    class Meta:
        model = Joueur
        fields = '__all__'


