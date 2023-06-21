from django import forms
from .models import Joueur
from equipe.models import Equipe



class JoueurForm(forms.ModelForm):
    # role = forms.ModelChoiceField(queryset=Role.objects.all(), required=False)
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), required=False)
    class Meta:
        model = Joueur
        fields = '__all__'
        
    # def init (self, args, **kwargs):
    #     super(JoueurForm, self).init(args, **kwargs)
    #     self.fields["equipe"].requierd = False



